import statistics
import sqlite3
import random
from scraper import colors, color_freq


# ==============================
#        SOLUTIONS
# ==============================

# QUESTION 1: MEAN COLOR (The color with the frequency closest to the average frequency)
avg_freq = len(colors) / len(color_freq) # Average Frequency = Total Shirts/Unique Colors
mean_color = min(color_freq, key=lambda x: abs(color_freq[x] - avg_freq))

# QUESTION 2: MOSTLY WORN (MODE COLOR)
mostly_worn = statistics.mode(colors)

# QUESTION 3: MEDIAN COLOR
sorted_items = sorted(color_freq.items()) # Sorts by color name: ASH, BLUE, BROWN...
median_pos = (len(colors) + 1) / 2 # Calculate the median position

# Cumulative frequency logic to find which color occupies that middle position
cumulative_sum = 0
median_color = None

for color, count in sorted_items:
    cumulative_sum += count
    if cumulative_sum >= median_pos:
        median_color = color
        break

# QUESTION 4: VARIANCE OF THE COLORS/FREQUENCIES
freq_list = list(color_freq.values())
variance = statistics.variance(freq_list)

# QUESTION 5: PROBABILITY OF RED
prob_red = color_freq.get('RED',0)/len(colors)

# QUESTION 6: SAVING COLOR AND FREQUENCY IN A DATABASE (SQLite --- Built-in, easy to run on any machine without setup) 
def save_to_db(data_dict):
    try:
        # creates a file named 'bincom.db' in your folder automatically
        conn = sqlite3.connect("bincom.db")
        cur = conn.cursor()
        
        cur.execute("CREATE TABLE IF NOT EXISTS color_freq (color TEXT, frequency INTEGER);")
        
        for color, count in data_dict.items():
            cur.execute("INSERT INTO color_freq (color, frequency) VALUES (?, ?)", (color, count))
            
        conn.commit()
        conn.close()
        print("Data saved to SQLite successfully.")
    except Exception as e:
        print(f"DB Error: {e}")


# QUESTION 7: RECURSIVE SEARCH ALGORITHM
def recursive_search(lst, target, index=0):
    if index >= len(lst):
        return False
    if lst[index] == target:
        return True
    return recursive_search(lst, target, index + 1)

# QUESTION 8: RANDOM 4-DIGIT BINARY TO BASE 10
binary_str = "".join([str(random.randint(0, 1)) for _ in range(4)])
base_10 = int(binary_str, 2)

# QUESTION 9: SUM OF FIRST 50 FIBONACCI SEQUENCE
def sum_fibonacci(n):
    a, b = 0, 1
    total = 0
    for _ in range(n):
        total += a
        a, b = b, a + b
    return total

# --- DISPLAY RESULTS ---
print(f"1. Mean Color: {mean_color}")
print(f"2. Mostly Worn Color: {mostly_worn}")
print(f"3. Median Color: {median_color}")
print(f"4. Variance of Frequencies: {variance:.2f}")
print(f"5. Probability of Red: {prob_red:.4f}")
print(f"7. Recursive Search (Found 10 in [1,3,5,4,10,6,8]): {recursive_search([1,3,5,4,6,8], 10)}")
print(f"8. Random Binary {binary_str} to Base 10: {base_10}")
print(f"9. Sum of first 50 Fibonacci Sequence: {sum_fibonacci(50)}")
