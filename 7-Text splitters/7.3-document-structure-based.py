from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text = """
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print(f"{self.name} is studying.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

# Example usage
student1 = Student("Alice", 20)
student1.study()
student1.sleep()
"""
# Initialize the text splitter1
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=100,
    chunk_overlap=0,
)
chunks = splitter.split_text(text)
print(f'len(chunks): {len(chunks)}')
print('chunks:')
for i, chunk in enumerate(chunks):
    print(f'Chunk {i}: {chunk}')