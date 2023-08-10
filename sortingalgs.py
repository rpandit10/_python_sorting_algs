import tkinter as tk
from tkinter import messagebox
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def merge_sort(arr):
    # Merge sort implementation
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

def selection_sort(arr):
    # Selection sort implementation
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


class SortingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting App")

        self.numbers_label = tk.Label(root, text="Enter a list of numbers (comma-separated):")
        self.numbers_label.pack(pady=10)

        self.numbers_entry = tk.Entry(root)
        self.numbers_entry.pack(pady=5)

        self.algorithm_label = tk.Label(root, text="Select a sorting algorithm:")
        self.algorithm_label.pack(pady=10)

        self.algorithm_var = tk.StringVar()
        self.algorithm_var.set("Bubble")  # Default selection
        self.algorithm_menu = tk.OptionMenu(root, self.algorithm_var, "Bubble", "Merge", "Selection")
        self.algorithm_menu.pack(pady=5)

        self.sort_button = tk.Button(root, text="Sort", command=self.sort_numbers)
        self.sort_button.pack(pady=10)

        self.output_label = tk.Label(root, text="")
        self.output_label.pack()

    def sort_numbers(self):
        numbers_str = self.numbers_entry.get()
        algorithm = self.algorithm_var.get()

        try:
            numbers = [int(num) for num in numbers_str.split(',')]
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid list of numbers.")
            return

        start_time = time.time()

        if algorithm == "Bubble":
            sorted_numbers = bubble_sort(numbers)
        elif algorithm == "Merge":
            sorted_numbers = merge_sort(numbers)
        elif algorithm == "Selection":
            sorted_numbers = selection_sort(numbers)

        end_time = time.time()
        sorting_time = end_time - start_time

        self.output_label.config(text=f"Sorted Numbers: {sorted_numbers}\nSorting Time: {sorting_time:.6f} seconds")

if __name__ == "__main__":
    root = tk.Tk()
    app = SortingApp(root)
    root.mainloop()
