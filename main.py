"""
## Introduction

Bonus project: Code Analyzer

Ramtin Ehsani, 97521018

"""

from utils.utils2 import get_program, get_filenames_in_dir


class CodeAnalyzer:
    def __init__(self, source_filenames: list,
                 filename_mapping=lambda x: x):

        self.source_filenames = source_filenames
        self.filename_mapping = filename_mapping

    def analyze(self):
        program = get_program(self.source_filenames)  # getting the program packages
        n = 1
        number_of_classes = 0
        logs_classes = []
        for package in program.packages:
            target_package = program.packages[package]
            _targets = target_package.classes
            number_of_classes += len(_targets)

            for target in _targets:
                target_class = _targets[target]
                class_name = target_class.name
                logs_classes.append(str(n) + ". " + class_name + ":")
                number_of_attributes = len(target_class.fields)
                number_of_methods = len(target_class.methods)
                logs_classes.append("\tno.attributes: " + str(number_of_attributes))
                public_attributes = []
                private_attributes = []
                protected_attributes = []
                class_counter = 0
                for field in target_class.fields:
                    target_field = target_class.fields[field]
                    mod = target_field.modifiers
                    if target_field.initializer is not None:
                        class_counter += 1
                    if len(mod) == 0:
                        public_attributes.append(field)
                    else:
                        if "private" in mod:
                            private_attributes.append(field)
                        elif "public" in mod:
                            public_attributes.append(field)
                        else:
                            protected_attributes.append(field)
                logs_classes.append("\t\tpublic: " + str(len(public_attributes)) + " " + str(public_attributes))
                logs_classes.append("\t\tprivate: " + str(len(private_attributes)) + " " + str(private_attributes))
                logs_classes.append("\t\tprotected: " + str(len(protected_attributes)) + " " + str(protected_attributes))
                logs_classes.append("\tno.methods: " + str(number_of_methods))
                logs_classes.append("\tno.classes accessed: " + str(class_counter))

                n += 1
        print("no.Classes: " + str(number_of_classes))
        for string in logs_classes:
            print(string)


if __name__ == '__main__':
    project = get_filenames_in_dir('./test')
    CodeAnalyzer(project).analyze()
