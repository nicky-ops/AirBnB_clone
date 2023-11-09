#!/usr/bin/python3

"""Defines the console"""
import re
import cmd
from models import storage
from shlex import split
from models.user import User
from models.state import State
from models.base_model import BaseModel
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
            exe = split(arg[:brackets.span()[0]])
            ret = [i.strip(",") for i in exe]
            ret.append(bracket.group())
            return ret
    else:
        exe = split(arg[:braces.span()[0]])
        ret = [i.strip(",") for i in exe]
        ret.append(braces.group())
        return ret

class HBNBCommand(cmd.Cmd):
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

def checkline(self):
    """Checks line if empty"""
    pass

def default(self, arg):
    """Default response to cmd module for invalid input"""
    argdict = {
            "all": self.cmd_all,
            "show": self.cmd_show,
            "destroy": self.cmd_destroy,
            "count": self.cmd_count,
            "update": self.cmd_update
        }
        cmd_match = re.search(r"\.", arg)
        if cmd_match is not None:
            argl = [arg[:cmd_match.span()[0]], arg[cmd_match.span()[1]:]]
            cmd_match = re.search(r"\((.*?)\)", argl[1])
            if cmd_match is not None:
                CMD = [argl[1][:cmd_same.span()[0]], cmd_match.group()[1:-1]]
                if CMD[0] in argdict.keys():
                    call = "{} {}".format(argl[0], CMD[1])
                    return argdict[CMD[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

def cmd_quit(self, arg):
    """Command to quit or exit the program"""
    return true

def cmd_EOF(self, arg):
    """Create a new class instance and print its id"""
    argl = parse(arg)
        if len(argl) == 0:
            print("** missing class name **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

def cmd_show(self, arg):
    """Shows the string representation of a class instance of a given id"""
    argl = parse(arg)
        odict = storage.all()
        if len(argl) == 0:
            print("** missing class name **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** missing instance id **")
        elif "{}.{}".format(argl[0], argl[1]) not in odict:
            print("** no instance found **")
        else:
            print(odict["{}.{}".format(argl[0], argl[1])])

def cmd_destroy(self, arg):
    """Delete a class instance of a given id."""
     argl = parse(arg)
        odict = storage.all()
        if len(argl) == 0:
            print("** missing class name **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** missing instance id **")
        elif "{}.{}".format(argl[0], argl[1]) not in odict.keys():
            print("** no instance found **")
        else:
            del odict["{}.{}".format(argl[0], argl[1])]
            storage.save()

def cmd_all(self, arg):
    """ Display string representations of all instances of a given class"""
    argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objectl = []
            for object2 in storage.all().values():
                if len(argl) > 0 and argl[0] == object2.__class__.__name__:
                    objectl.append(obect2j.__str__())
                elif len(argl) == 0:
                    objectl.append(object2.__str__())
            print(objectl)

def cmd_count(self, arg):
    """Retrieve the number of instances of a given class"""
     argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

def cmd_update(self, arg):
    """Update a class instance of a given id"""
    argl = parse(arg)
    odict = storage.all()
    
    if len(argl) == 0:
            print("** missing class name **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** missing instance id **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in odict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** missing attribute name **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** missing value **")
                return False
        if len(argl) == 4:
            obj = odict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valuetype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valuetype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = odict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valuetype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valuetype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
