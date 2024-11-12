import sqlite3


connection = sqlite3.connect('leaderboard.db')

class Leaderboard:

    def __init__(self):
        self.cursor = connection.cursor()
        self.gameName = 'leaderboard'
        self.cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {self.gameName} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL, points TEXT NOT NULL, date TEXT NOT NULL)''')
        
    
    def add_entry(self, name, points):
        self.cursor.execute(f"INSERT INTO {self.gameName} (name, points, date) VALUES (?,?, DATETIME('now'))", (name, points))
        connection.commit()

    def remove_entry(self, name, points):
        self.cursor.execute(f"DELETE FROM {self.gameName} WHERE name = ? AND points = ?", (name, points))
        connection.commit()

    def update_entry(self, old_name, old_points, new_name, new_points):
        self.cursor.execute(f"UPDATE {self.gameName} SET name = ?, points = ? WHERE name = ? AND points = ?", (new_name, new_points, old_name, old_points))
        connection.commit()
    
    def get_all_entries(self):
        self.cursor.execute(f"SELECT * FROM {self.gameName} ORDER BY points DESC")
        return self.cursor.fetchall()
    
    def get_top_entries(self, limit=10):
        self.cursor.execute(f"SELECT * FROM {self.gameName} ORDER BY points DESC LIMIT ?", (limit,))
        return self.cursor.fetchall()
    
    def get_average_points(self):
        self.cursor.execute(f"SELECT AVG(points) FROM {self.gameName}")
        return self.cursor.fetchone()[0]

class gameLeaderboard(Leaderboard):
    def __init__(self, gameName):
        super().__init__()
        self.gameName = gameName
        self.cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {self.gameName} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL, points TEXT NOT NULL, date TEXT NOT NULL)''')


