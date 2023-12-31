import re


def main():
    with open('input.txt') as inputtxt:
        lines = inputtxt.readlines()

        sum_games = 0
        sum_multiples = 0

        for i, line in enumerate(lines):
            game_id = str(i + 1)
            assert line.startswith('Game ' + game_id + ': ')
            start_len = len('Game ' + game_id + ': ')
            rem = line[start_len:]
            red_ss = 0
            green_ss = 0
            blue_ss = 0
            for sets in rem.split(';'):
                red = 0
                green = 0
                blue = 0
                for ssg in sets.split(','):
                    ssg_strip = ssg.strip()
                    if ssg_strip.endswith('blue'):
                        match = re.fullmatch('(\\d+) blue', ssg_strip)
                        assert match is not None
                        blue = int(match.group(1))
                    elif ssg_strip.endswith('green'):
                        match = re.fullmatch('(\\d+) green', ssg_strip)
                        assert match is not None
                        green = int(match.group(1))
                    elif ssg_strip.endswith('red'):
                        match = re.fullmatch('(\\d+) red', ssg_strip)
                        assert match is not None
                        red = int(match.group(1))
                red_ss = max(red_ss, red)
                green_ss = max(green_ss, green)
                blue_ss = max(blue_ss, blue)
            if red_ss <= 12 and green_ss <= 13 and blue_ss <= 14:
                sum_games += i + 1
            sum_multiples += red_ss * green_ss * blue_ss
        print('part a:', sum_games)
        print('part b:', sum_multiples)


if __name__ == "__main__":
    main()
