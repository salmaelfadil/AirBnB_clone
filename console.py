#!/usr/bin/python3
"""
the entry point of the command interpreter
"""
import cmd
import json
import re
import models
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    class definiation
    """
    prompt = '(hbnb) '
    classes = ['BaseModel', 'User', 'Place', 'State',
               'City', 'Amenity', 'Review']
    attrs = ["updated_at", "created_at", "id"]
    specs = ["\'", "\""]

    def do_EOF(self, line):
        """quit when ctrl +D """
        print()
        return True

    def do_quit(self, line):
        """quit when type quit"""
        return True

    def emptyline(self):
        """do nothing when pass empty line"""
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel
        """
        if not line:
            print("** class name missing **")
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(line)()
            print(new_instance.id)
            new_instance.save()

    def do_show(self, line):
        """
        Prints the string representation of an instance based
        on the class name and id
        """
        args = line.split()
        if not line:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        new_instance = "{}.{}".format(args[0], args[1])
        if new_instance not in storage.all().keys():
            print("** no instance found **")
            return
        else:
            print(storage.all()["{}.{}".format(args[0], args[1])])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if not line:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            new_instance = "{}.{}".format(args[0], args[1])
            if new_instance not in storage.all():
                print("** no instance found **")
            else:
                models.storage.all().pop(new_instance)
                models.storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances"""
        args = line.split()
        result = []
        if len(args) != 0:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
                return
            else:
                for _, value in storage.all().items():
                    if type(value).__name__ == args[0]:
                        result.append(value.__str__())
        else:
            for _, value in storage.all().items():
                result.append(value.__str__())
        print(result)

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        arg = line.split()
        if not line:
            print("** class name missing **")
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        elif arg[0] + "." + arg[1] not in storage.all().keys():
            print("** no instance found **")
            return
        elif len(arg) == 2:
            print("** attribute name missing **")
            return
        elif len(arg) == 3:
            print("** value missing **")
            return
        else:
            object = models.storage.all()
            key = "{}.{}".format(arg[0], arg[1])
            if key in object:
                if arg[2] not in self.attrs:
                    if arg[3][0] in self.specs and arg[3][-1] in self.specs:
                        setattr(object[key], arg[2], str(arg[3][1: -1]))
                    else:
                        setattr(object[key], arg[2], str(arg[3]))
                    storage.save()
            else:
                print("** no instance found **")
                return

    def do_count(self, line):
        """Retrieve the number of instances of a class"""
        count = 0
        inst = storage.all()
        arg = line.split()
        for inst in inst.values():
            if inst.__class__.__name__ == arg[0]:
                count += 1
        print(count)

    def default(self, line):
        """Default function that handles all the method"""
        found = re.search(r"\.", line)
        if found is not None:
            arg = [line[:found.span()[0]], line[found.span()[1]:]]
            found = re.search(r"\((.*?)\)", arg[1])
            if found is not None:
                comm = [arg[1][:found.span()[0]], found.group()[1:-1]]
                if comm[0] == "count":
                    final = "{} {}".format(arg[0], comm[1])
                    return self.do_count(final)
                elif comm[0] == "all":
                    final = "{} {}".format(arg[0], comm[1])
                    return self.do_all(final)
                elif comm[0] == "show":
                    final = "{} {}".format(arg[0], comm[1])
                    return self.do_show(final)
                elif comm[0] == "destroy":
                    final = "{} {}".format(arg[0], comm[1])
                    return self.do_destroy(final)
                elif comm[0] == "update":
                    final = "{} {}".format(arg[0], comm[1])
                    return self.do_update(final)
        print("*** Unknown syntax: {}".format(line))
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
