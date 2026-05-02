import tkinter as tk
from random import randint, choice


class Pet:
    def __init__(self, species):
        self.species = species

    def get_angry(self):
        return f"Твій {self.species} розізлився і вкусив тебе!"


class Player:
    def __init__(self, name):
        self.name = name
        self.money = 150
        self.hp = 100
        self.inventory = []  # список тваринок

    def go_work(self):
        salary = randint(30, 60)
        self.money += salary
        self.hp -= 15
        return salary

    def sleep(self):
        self.hp += 20
        if self.hp > 100:
            self.hp = 100
        return "Ти добре виспався!"


me = Player("Maxim")


def update_gui(text):
    label_msg.config(text=text)
    label_stats.config(text=f"Гроші: {me.money}$ | Здоров'я: {me.hp} | Тварин: {len(me.inventory)}")

    if me.hp <= 0:
        label_msg.config(text="Кінець гри! Ти занадто втомився...", fg="red")
        btn_work.config(state="disabled")
        btn_rest.config(state="disabled")
        btn_buy.config(state="disabled")


def work_handler():
    earned = me.go_work()
    update_gui(f"Ти попрацював і заробив {earned}$")


def rest_handler():
    msg = me.sleep()
    update_gui(msg)


def buy_handler():
    try:
        if me.money < 70:
            update_gui("Недостатньо грошей! Треба 70$")
            return

        me.money -= 70
        pet_types = ["Пес", "Кіт", "Хом'як", "Папуга"]
        new_pet = Pet(choice(pet_types))
        me.inventory.append(new_pet)

        if randint(1, 4) == 1:  # 25% шанс що вкусить
            me.hp -= 10
            update_gui(new_pet.get_angry())
        else:
            update_gui(f"Круто! Тепер у тебе є {new_pet.species}")

    except Exception as e:
        print("Помилка в магазині:", e)


root = tk.Tk()
root.title("Симулятор життя v1.0")
root.geometry("350x400")

label_msg = tk.Label(root, text="Вітаємо у грі!", font=("Verdana", 11), pady=15)
label_msg.pack()

label_stats = tk.Label(root, text="Гроші: 150 | Здоров'я: 100 | Тварин: 0", font=("Verdana", 10, "bold"))
label_stats.pack(pady=5)

btn_work = tk.Button(root, text="Йти на роботу", width=25, bg="lightgreen", command=work_handler)
btn_work.pack(pady=5)

btn_rest = tk.Button(root, text="Відпочити (+20 HP)", width=25, bg="lightblue", command=rest_handler)
btn_rest.pack(pady=5)

btn_buy = tk.Button(root, text="Купити тваринку (70$)", width=25, command=buy_handler)
btn_buy.pack(pady=5)

btn_exit = tk.Button(root, text="Вийти з гри", width=25, command=root.destroy, fg="red")
btn_exit.pack(pady=20)

root.mainloop()


