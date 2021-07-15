"""Entry point for this job"""
import sys
import pandas



def main(country):
    print("Country:", country)
    print("Pandas:", pandas)
    print("Test job run successfully")


if __name__ == '__main__':
    main(country=sys.argv[1])
