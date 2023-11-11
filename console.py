#!/usr/bin/python3

"""Defines the HBnB console."""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    braces = re.search(r"\{(.*?)\}", arg)
    bracket = re.search(r"\[(.*?)\]", arg)
    if braces is None:
        if bracket is None:
            return [i.strip(",") for i in split(arg)]
        else:
            exe = split(arg[:bracket.span()[0]])
            ret = [i.strip(",") for i in exe]
            ret.append(bracket.group())
            return ret
    else:
        exe = split(arg[:braces.span()[0]])
        ret = [i.strip(",") for i in exe]
        ret.append(braces.group())
        return ret


class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command interpreter."""
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Checks line if empty"""
        pass

    def default(self, arg):
        """Default response to cmd module for invalid input"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        cmd_match = re.search(r"\.", arg)
        if cmd_match is not None:
            arg2 = [arg[:cmd_match.span()[0]], arg[cmd_match.span()[1]:]]
            cmd_match = re.search(r"\((.*?)\)", arg2[1])
            if cmd_match is not None:
                C_MD = [argl[1][:cmd_match.span()[0]], cmd_match.group()[1:-1]]
                if C_MD[0] in argdict.keys():
                    call = "{} {}".format(arg2[0], C_MD[1])
                    return argdict[C_MD[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Command to quit or exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print("")
        return True

    def do_create(self, arg):
        """Create a new class instance and print its id"""
        arg2 = parse(arg)
        if len(arg2) == 0:
            print("** class name missing **")
        elif arg2[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg2[0])().id)
            storage.save()

    def do_show(self, arg):
        """Shows the string representation of a class instance of a given id"""
        arg2 = parse(arg)
        odict = storage.all()
        if len(arg2) == 0:
            print("** class name missing **")
        elif arg2[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg2) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg2[0], arg2[1]) not in odict:
            print("** no instance found **")
        else:
            print(odict["{}.{}".format(arg2[0], arg2[1])])

    def do_destroy(self, arg):
        """Destroys a class instance of a given id."""
        arg2 = parse(arg)
        odict = storage.all()
        if len(arg2) == 0:
            print("** class name missing **")
        elif arg2[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg2) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg2[0], arg2[1]) not in odict.keys():
            print("** no instance found **")
        else:
            del odict["{}.{}".format(arg2[0], arg2[1])]
            storage.save()

    def do_all(self, arg):
        """Display string representations of all instances of a given class"""
        arg2 = parse(arg)
        if len(arg2) > 0 and arg2[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objectl = []
            for object2 in storage.all().values():
                if len(arg2) > 0 and arg2[0] == object2.__class__.__name__:
                    objectl.append(object2.__str__())
                elif len(arg2) == 0:
                    objectl.append(object2.__str__())
            print(objectl)

    def do_count(self, arg):
        """Retrieve the number of instances of a given class."""
        arg2 = parse(arg)
        count = 0
        for object1 in storage.all().values():
            if arg2[0] == object1.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Update a class instance of a given id"""
        arg2 = parse(arg)
        odict = storage.all()

        if len(arg2) == 0:
            print("** class name missing **")
            return False
        if arg2[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg2) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg2[0], arg2[1]) not in odict.keys():
            print("** no instance found **")
            return False
        if len(arg2) == 2:
            print("** attribute name missing **")
            return False
        if len(arg2) == 3:
            try:
                type(eval(arg2[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg2) == 4:
            obj = odict["{}.{}".format(arg2[0], arg2[1])]
            if arg2[2] in obj.__class__.__dict__.keys():
                valuetype = type(obj.__class__.__dict__[arg2[2]])
                obj.__dict__[arg2[2]] = valuetype(arg2[3])
            else:
                obj.__dict__[arg2[2]] = arg2[3]
        elif type(eval(arg2[2])) == dict:
            obj = odict["{}.{}".format(arg2[0], arg2[1])]
            for m, n in eval(arg2[2]).items():
                if (m in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[m]) in {str, int, float}):
                    valuetype = type(obj.__class__.__dict__[m])
                    obj.__dict__[m] = valuetype(n)
                else:
                    obj.__dict__[m] = n
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
