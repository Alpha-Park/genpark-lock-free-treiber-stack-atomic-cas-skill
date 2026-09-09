"""Example usage for Treiber Stack Skill."""
from client import TreiberStack

def main():
    print("Executing Treiber Stack...")
    stack = TreiberStack()
    stack.push(100)
    stack.push(200)
    stack.push(300)

    print("Stack items:", stack.to_list())
    v1 = stack.pop()
    v2 = stack.pop()
    print("Popped values:", v1, v2)
    assert v1 == 300 and v2 == 200
    print("Treiber Stack verified successfully!")

if __name__ == "__main__":
    main()
