from friends_module.config.mysqlconnection import connectToMySQL

class Friend:
    def get_all_friends(self):
        mysql = connectToMySQL('full_friends')
        query = "SELECT * FROM myfriends"
        result = mysql.query_db(query)
        return result

    def create_friend(self, form):
        mysql = connectToMySQL('full_friends')
        query = "INSERT INTO myfriends (first_name, last_name, age, friend_since, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(friend_since)s, NOW(), NOW())"
        data = {
                 'first_name': form['first_name'],
                 'last_name':  form['last_name'],
                 'age': form['age'],
                 'friend_since': form['friend_since']
               }
        mysql.query_db(query, data)
        return self

    def clear_db(self):
        mysql = connectToMySQL('full_friends')
        query = "TRUNCATE TABLE myfriends"
        mysql.query_db(query)
        return self
