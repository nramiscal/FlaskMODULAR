from flask import render_template, redirect
from friends_module.models.friend import Friend

friend = Friend()

class Friends:
    def index(self):
        friends = friend.get_all_friends()
        return render_template('index.html', my_friends=friends)

    def create(self, form):
        friend.create_friend(form)
        return redirect('/')


    def clear_db(self):
        friend.clear_db()
        return redirect('/')
