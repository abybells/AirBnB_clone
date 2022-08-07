#!/usr/bin/python3
"""Module for console class"""


import cmd
import json
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
# from models import storage


class HBNBCommand(cmd.Cmd):
    """command line terminal for HBNB"""

    intro = "WELCOME TO HBNB SHELL"
    prompt = '(hbnb) '
    MODELS = [Amenity, BaseModel, City, Place, Review, State, User]

    def do_quit(self, line):
        """command to exit the command line"""
        return True

    def do_EOF(self, line):
        """command passes End Of File command
        to exit the command line"""
        return True

    def precmd(self, line):
        parse_line = line.rstrip('\n')
        if line:
            if line[-1] == ")" and "." in line:
                parse_line = ""
                line_arr = line.split(".")
                class_name = line_arr[0]
                cmd_arr = line_arr[1].split('(')
                cmd_name = cmd_arr[0]
                cmd_arg = cmd_arr[1][:-1]
                cmd_arg_arr = cmd_arg.split(", ")
                cmd_arg = " ".join(cmd_arg_arr)
                parse_line = cmd_name + " " + class_name + " " + cmd_arg
        return super().precmd(parse_line)

    def emptyline(self):
        """command to handle empty line"""
        return

    def check_for_id(self, id_dict, id_instance):
        """checks list of keys to find an id"""
        for ind_id in id_dict:
            if id_instance == ind_id.split(".")[1]:
                return 1
        return 0

    def do_create(self, line):
        """create class instance based on class name
        Usage: create <class> or <class>.create()
        Ex: create BaseModel"""

        if len(line) == 0:
            print('** class name missing **')
            return
        class_name = line.split()[0]
        for model in self.MODELS:
            if class_name == model.__name__:
                model_instance = model()
                print(model_instance.id)
                model_instance.save()
                return
        print("** class doesn't exist **")

    def do_show(self, line):
        """Print string representation of a particular
        instance based on class name and id
        Usage: show <class> <id> or <class>.show(<id>)
        Ex: show BaseModel 1234-1234-1234"""
        if len(line) == 0:
            print('** class name missing **')
            return
        split_line = line.split()
        class_name = split_line[0]
        if len(split_line) > 1:
            model_id = split_line[1]
        else:
            print("** instance id missing **")
            return

        for model in self.MODELS:
            if class_name == model.__name__:
                storage.reload()
                files = storage.all()
                for k in files:
                    split_key = k.split(".")
                    if (len(model_id) - len(model_id.strip('\"')) == 2 or
                            len(model_id) - len(model_id.strip('\"')) == 2):
                        model_id = model_id.strip('\"\'')
                    if split_key[0] == class_name and split_key[1] == \
                            model_id:
                        model_instance = model(**files[k].to_dict())
                        print(model_instance)
                        return
                print("** no instance found **")
                return
        print("** class doesn't exist **")

    def do_destroy(self, line):
        """Delete instance based on class name and id
        Usage: destroy <class> <id> or <class>.destroy(<id>)
        Ex: destroy BaseModel 1234-1234-1234"""
        if len(line) == 0:
            print('** class name missing **')
            return
        split_line = line.split()
        class_name = split_line[0]
        if len(split_line) > 1:
            model_id = split_line[1]
        else:
            print("** instance id missing **")
            return

        for model in self.MODELS:
            if class_name == model.__name__:
                storage.reload()
                files = storage.all()
                dict_filter = {}
                if self.check_for_id(files.keys(), model_id):
                    for k in files.keys():
                        if model_id not in k:
                            dict_filter[k] = files[k].to_dict()
                    with open("file.json", mode='w', encoding='utf-8')\
                            as json_file:
                        json.dump(dict_filter, json_file)
                else:
                    print("** no instance found **")
                return
        print("** class doesn't exist **")

    def do_all(self, line):
        """Print string representation of all
        instance based or not on class name
        Usage: all <class> | all or <class>.all()
        Ex: all BaseModel or all"""
        my_list = []
        models.storage.reload()
        files = storage.all()
        if line:
            class_name = line.split()[0]
            for model in self.MODELS:
                if class_name == model.__name__:
                    for item in files:
                        sub_items = files[item].to_dict()
                        if sub_items["__class__"] == class_name:
                            sub_instance = model(**sub_items)
                            my_list.append(str(sub_instance))
                    print(my_list)
                    return
            print("** class doesn't exist **")
        else:
            for item in files:
                sub_items = files[item].to_dict()
                for model in self.MODELS:
                    if sub_items["__class__"] == model.__name__:
                        sub_instance = model(**sub_items)
                        my_list.append(str(sub_instance))
            print(my_list)

    def do_update(self, line):
        """update an instance based on class name and id
        updating existing attributes or adding new ones
        Usage: update <class> <id> <attribute> <value>
        or <class>.update(<id>, <attribute>, <value>)
        attribute and value can also be replaced with a dictionary of
        attributes and values.
        Ex: update BaseModel 1234-1234-1234 email 'aibnb@mail.com'"""
        if len(line) == 0:
            print('** class name missing **')
            return
        split_line = line.split()
        class_name = split_line[0]
        if len(split_line) > 1:
            model_id = split_line[1]
        else:
            print("** instance id missing **")
            return

        for model in self.MODELS:
            if class_name == model.__name__:
                # storage.reload()
                files = storage.all()
                for k in files:
                    split_key = k.split(".")
                    if (len(model_id) - len(model_id.strip('\"')) == 2 or
                            len(model_id) - len(model_id.strip('\"')) == 2):
                        model_id = model_id.strip('\"\'')
                    if split_key[0] == class_name and split_key[1] == model_id:
                        model_instance = model(**files[k].to_dict())
                        if len(split_line) > 2:
                            attr = split_line[2]
                        else:
                            print("** attribute name missing **")
                            return
                        if len(split_line) > 3:
                            value = split_line[3]
                        else:
                            print("** value missing **")
                            return
                        setattr(model_instance, attr, value)

                        storage.reload()
                        files = storage.all()
                        update = {}
                        if self.check_for_id(files.keys(), model_id):
                            for k in files.keys():
                                if model_instance.id in k:
                                    update[k] = model_instance.to_dict()
                                else:
                                    update[k] = files[k].to_dict()
                            with open("file.json", mode='w', encoding='utf-8')\
                                    as json_file:
                                json.dump(update, json_file)
                                return
                print("** no instance found **")
                return
        print("** class doesn't exist **")

    def do_count(self, line):
        """Print count of instances of a particular class
        Usage: <class>.count() or count <class>"""
        if line:
            class_name = line.split()[0]
            for model in self.MODELS:
                if class_name == model.__name__:
                    break
            else:
                print("** class doesn't exist **")
                return

            storage.reload()
            count = 0
            files = storage.all()
            for k in files.keys():
                if k.split(".")[0] == class_name:
                    count += 1
            print(count)
        else:
            print('** class name missing **')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
