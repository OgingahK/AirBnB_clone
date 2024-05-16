#!/usr/bin/python3
"""Defines the command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json

class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter"""

    prompt = " (hbnb) "


    def default(self, line):
        """If it cannot catch commands then it will match them"""
        # print("DEF:::", line)
        self.precmd(line)


    def precmd(self, line):
        """Get the line before interpretor"""
        # print("PRECMD:::", line)
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        class_name = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

            attr_and_value = ""
            if method == "update" and attr_or_dict:
                match_dict = re.search('^({.*})$', attr_or_dict)
                if match_dict:
                    self.update(class_name, uid, match_dict.group(1))
                    return ""
                match_attr_and_value = re.search('^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
                if match_attr_and_value:
                    attr_and_value = (match_attr_and_value.group(1) or "")
                    command = method + " " + class_name + " " + uid + attr_and_value
                    self.onecmd(command)
                    return command

    def dict_update(self, class_name, uid, dict_s):
        """Method helper for update() with dictonary."""
        s = dict_s.replace("'", '"')
        d = json.loads(s)
        if not class_name:
            print("** class doesn't exist **")
        elif uid is NONE:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(class_name, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[class_name]
                for attribute, value in d.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                        setattr(storage.all()[key], attribute, value)
                        storage.all()[key].save()

    def do_EOF(self, line):
        """Tackles end of line character"""
        print()
        return True

    def do_quit(self, line):
        """Quits the program"""
        return True

    def empty_line(self):
        """Ignores ENTER"""
        pass

    def do_create(self, line):
        """Creates an instance"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)

    def do_show(self, line):
        """Prints the string representation of an instance."""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            words = line.split(' ')
            if words[0] not in storage.classes:
                print("** class doesn't exist **")
            elif len(words) > 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_count(self, line):
        """Counts the instances of a class"""
        words = line.split(' ')
        if not words[0]:
            print("** class namemissing **")
        elif words[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            matches = [k for k in storage.all() if k.starts_with(words[0] + '.')]
            print(len(matches))

    def do_update(self, line):
        """Updates an instance"""
        if line == "" or line is None:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                    else:
                        value = value.replace('"', '')
                        attributes = storage.attributes()[classname]
                        if attribute in attributes:
                            value = attributes[attribute](value)
                        elif cast:
                            try:
                                value = cast(value)
                            except ValueError:
                                pass # fine, stay string then
                            setattr(storage.all()[key], attribute, value)
                            storage.all()[key].save()


    if __name__ == '__main__':
        HBNBCommand().cmdloop()
