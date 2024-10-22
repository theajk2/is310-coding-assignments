from rich.console import Console
from rich.table import Table

console = Console()
console.print("Here are a couple books that I love:", style ="purple")
table = Table(title = "Favorite Book")
table.add_column("Title")
table.add_column("Genre")
table.add_column("Year Published")
table.add_row("The Priory of the Orange Tree", "fantasy", "2019")
table.add_row("Challenger Deep","realistic fiction", "2016")
table.add_row("Blue Lily, Lily Blue", "magical realism","2014")
console.print(table)
console.print("\n[bold orange]What's your favorite book? Input them:[/bold orange]")
def save_text(table):
      var = open('book_list.txt', 'a')  
      for row_index in range(len(table.column[0]._cells)):
              content = [str(column._cells[row_index]) for column in table.column]
              var.write("".join(content) + "\n")
              print(content)
              
def addBook():
        oldTable = Table(title = "Favorite Book")
        oldTable.add_column("Title", no_wrap = True)
        oldTable.add_column("Genre", no_wrap = True)
        oldTable.add_column("Year Published", no_wrap = True)
        console.print("What is this book titled?")
        while True:
                title = input("Enter the title of your book!")
                save_text(oldTable)
                console.print("Your book title has been saved!")
                while True:
                        genre = input("Enter the genre of your book!")
                        save_text(oldTable)
                        console.print("Your book genre has been saved!")
                        while True:
                                release_year = input("Enter the year your book was released!")
                                save_text(oldTable)
                                console.print("Your release date has been saved!")
        console.print()
addBook()