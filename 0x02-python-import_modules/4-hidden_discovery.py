#!/usr/bin/python3
import hidden_4


def main():
    for i in range(len(dir(hidden_4))):
        if dir(hidden_4)[i][:2] != "__":
            print(dir(hidden_4)[i])


if __name__ == "__main__":
    main()
