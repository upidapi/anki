import random
import os
import genanki
import json

"""
nix-shell -p python3Packages.genanki --command "python src/main.py"
"""

def pp(data):
    print(json.dumps(data, indent=4))


def name_to_id(name):
    random.seed(name)
    return random.randrange(1 << 30, 1 << 31)


# python3 -c "import random; print(random.randrange(1 << 30, 1 << 31))"

# 1398612117


os.chdir(os.path.dirname(os.path.abspath(__file__)))

style = open("style.css").read()

my_model = genanki.Model(
    1607392319,
    "Model",
    fields=[
        {"name": "Question"},
        {"name": "Answer"},
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{Question}}",
            "afmt": '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ],
    css=style,
)


def parse(lines: list[str], file_path: str):
    parsed = []

    # a list of all labels cuactive and their content

    """
    word | translation

    test:
        hello | hi

        something:
            goodbye | bye       

        sup | huh

    que | what

    res = [
        "word | translation",
        (
            "test",
            [
                "hello | hi",
                ("something", ["goodbye | bye"]),
                "sup | huh",
            ],
        ),
    ]
    """

    for i, line in enumerate(lines):
        raw_indent_lvl = len(line) - len(line.lstrip())

        line = line.strip()

        # ignore blank lines and comments
        if line == "":
            continue
        if line.startswith("#"):
            continue

        if raw_indent_lvl % 4 != 0:
            raise Exception(
                f"indent not multiple of 4 at line {i}:{file_path}"
            )

        indent_lvl = raw_indent_lvl // 4

        lvl = 0
        part = parsed
        while lvl < indent_lvl:
            if not part or isinstance(part[-1], str):
                raise Exception(
                    f"line is over indented at {i}:{file_path}"
                )

            part = part[-1][1]
            lvl += 1

        if line.endswith(":"):
            # adding :: in the name creates a sub dir
            # if "::" in line:
            #     raise Exception("name cant have :: in it")

            part.append((line[:-1], []))
        else:
            part.append(line)

    return parsed


parsed_lines_type = list[str | tuple[str, "parsed_lines_type"]]


def create_decks(
    parsed_lines: parsed_lines_type, name_dir: list[str]
):
    deck_name = "::".join(name_dir)
    deck = genanki.Deck(name_to_id(deck_name), deck_name)
    decks = [deck]

    for thing in parsed_lines:
        if isinstance(thing, tuple):
            category_name, category_data = thing
            
            decks += create_decks(
                category_data, [*name_dir, category_name]
            )

            continue

        word, translation = map(str.strip, thing.split("|"))

        # out += f"{translation} | {word}\n"

        note = genanki.Note(
            model=my_model, fields=[translation, word]
        )

        decks[0].add_note(note)

    return decks


# def parse_file(lines):
#     decks = []
#     out = ""
#
#     deck = None
#
#     for raw_line in lines:
#         print(raw_line)
#         line = raw_line.strip()
#
#         if line == "":
#             continue
#
#         if line.startswith("#"):
#             continue
#
#         if not raw_line.startswith("    "):
#             if deck is not None:
#                 decks.append(deck)
#
#             deck = genanki.Deck(name_to_id(line), line)
#             continue
#
#         line = line.strip()
#         # print(f"\"{line}\"")
#
#         word, translation = map(str.strip, line.split("|"))
#
#         # out += f"{translation} | {word}\n"
#
#         note = genanki.Note(
#             model=my_model, fields=[translation, word]
#         )
#
#         deck.add_note(note)
#
#     if deck is not None:
#         decks.append(deck)
#
#     return decks


def parse_files():
    data_dir = "../data/part_3"
    data_dirs = os.listdir(data_dir)
    for data_file in data_dirs:
        base_name = data_file[: -len(".txt")]
        # name = " ".join(base_name.split("_"))
        file_path = f"{data_dir}/{data_file}"
        print(f"parsing {file_path}")
        with open(file_path) as f:
            try: 
                decks = create_decks(
                    parse(f.readlines(), file_path),
                    ["generated"]
                )
            except Exception:
                print("   file failed")
                pass

        genanki.Package(decks).write_to_file(
            f"./../out/{base_name}.apkg"
        )


parse_files()
