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

    def default(self, line):
        """
        Handling the default behaviour
        """
        full_match = re.search(r'[A-Z][a-z]+\.\w+\((.*?)\)', line)
        met_match = re.search(r'(?<=\.)\w+\((.*?)\)', line)
        met_dict = {
                "all": self.do_all,
                "show": self.do_show,
                "count": self.do_count,
                "update": self.do_update,
                "destroy": self.do_destroy,
                "create": self.do_create
                }
        if full_match and met_match:
            cls = re.search(r'^[A-Z][a-z]+', full_match.group(0))
            met = re.search(r'^\w+(?=\()', met_match.group(0))
            if not met or not cls:
                print("** Unknown syntax:", line)
            else:
                cls = cls.group(0)
                met = met.group(0)
                if cls in self.classes and met in met_dict.keys():
                    pattern = r'(?<=\()(.+?)(?=\))'
                    arg_search = re.search(pattern, met_match.group(0))
                    if arg_search:
                        args = arg_search.group(0).split(",")
                        args = " ".join([arg.strip("()\"' ") for arg in args])
                        met_dict[met](cls + " " + args)
                    else:
                        met_dict[met](cls)
                elif cls not in self.classes:
                    print("** class doesn't exist **")
                else:
                    print("** Unknown syntax:", line)
        else:
            print(" *** Unknown syntax:", line)

    def do_count(self, line):
        """
        retrieve the number of instances of a class
        """
        inst = storage.all()
        arg = line.split()
        count = 0
        for instance in inst.values():
            if instance.__class__.__name__ == arg[0]:
                count += 1
        print(count)

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
