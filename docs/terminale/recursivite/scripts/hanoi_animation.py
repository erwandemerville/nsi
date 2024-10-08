import tkinter as tk

# Fonction pour résoudre les Tours de Hanoï
def hanoi(n, source, target, auxiliary, source_name, target_name, auxiliary_name):
    if n > 0:
        # Déplacer n-1 disques de la source à l'auxiliaire, en utilisant la cible comme tour auxiliaire
        hanoi(n - 1, source, auxiliary, target, source_name, auxiliary_name, target_name)

        # Déplacer un disque de la source à la cible
        disk = source.pop()
        target.append(disk)

        # Enregistrement de l'action
        actions.append(f"Déplacer le disque de {source_name} vers {target_name}")

        # Mettre à jour l'affichage après chaque déplacement
        update_display()
        root.after(delay)  # Délai en millisecondes pour voir le déplacement

        # Déplacer les n-1 disques restants de l'auxiliaire à la cible, en utilisant la source comme tour auxiliaire
        hanoi(n - 1, auxiliary, target, source, auxiliary_name, target_name, source_name)

# Fonction pour mettre à jour l'affichage
def update_display():
    canvas.delete("all")
    for i in range(3):
        x = i * tower_spacing + tower_center
        canvas.create_rectangle(x - tower_width // 2, canvas_height - base_height,
                                x + tower_width // 2, canvas_height, fill="gray")
        for j, disk in enumerate(towers[i]):
            width = base_disk_width + disk * disk_width_increment
            x0 = x - width // 2
            x1 = x0 + width
            y0 = canvas_height - base_height - (j + 1) * disk_height
            y1 = y0 + disk_height
            canvas.create_rectangle(x0, y0, x1, y1, fill="blue")

    action_text.delete(1.0, tk.END)
    for action in actions:
        action_text.insert(tk.END, action + "\n")
    root.update()

# Fonction appelée lorsque l'utilisateur clique sur le bouton "Résoudre"
def solve_hanoi():
    global towers, actions
    num_disks = int(num_disks_var.get())
    towers = [list(range(num_disks, 0, -1)), [], []]
    actions = []
    action_text.delete(1.0, tk.END)
    update_display()
    root.after(delay)  # Délai en millisecondes pour voir le déplacement
    hanoi(num_disks, towers[0], towers[2], towers[1], "A", "C", "B")

# Paramètres pour l'affichage des tours
delay = 500
tower_spacing = 250
tower_center = 200
tower_width = 10
base_height = 10
base_disk_width = 200
disk_width_increment = 10
disk_height = 20
canvas_height = 400
towers = [[], [], []]

# Paramètres de la fenêtre Tkinter
root = tk.Tk()
root.title("Tours de Hanoï")
canvas = tk.Canvas(root, width=900, height=400)
canvas.pack()

# Paramètres de la tour
num_disks_var = tk.StringVar()
num_disks_label = tk.Label(root, text="Nombre de disques:")
num_disks_label.pack()
num_disks_entry = tk.Entry(root, textvariable=num_disks_var)
num_disks_entry.pack()

# Bouton pour résoudre les Tours de Hanoï
solve_button = tk.Button(root, text="Résoudre", command=solve_hanoi)
solve_button.pack()

# Affichage des actions
action_text = tk.Text(root, height=10, width=40)
action_text.pack()

root.mainloop()
