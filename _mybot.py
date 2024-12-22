import telebot

TOKEN = '8127842023:AAGAS2_VNTTPqTyZTZud8qTNmiBJrB1SvKE'

bot = telebot.TeleBot(TOKEN)

# In-Memory Task List (replace with database for persistent storage)
tasks = []

# Start Command
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, "Welcome to Persist Ventures Operations Bot! Use /help to see available commands.")

# Help Command
@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = (
        "Available Commands:\n"
        "/start - Welcome message\n"
        "/help - List available commands\n"
        "/addtask <task> - Add a task\n"
        "/viewtasks - View all tasks\n"
        "/removetask <task> - Remove a specific task\n"
        "/completetask <task> - Mark a task as completed\n"
        "/cleartasks - Clear all tasks"
    )
    bot.reply_to(message, help_text)

# Add Task Command
@bot.message_handler(commands=['addtask'])
def add_task_command(message):
    task = message.text.replace('/addtask', '').strip()
    if task:
        tasks.append(task)
        bot.reply_to(message, f"✅ Task added: '{task}'")
    else:
        bot.reply_to(message, "❗ Usage: /addtask <task> - Please specify the task to add.")

# View Tasks Command
@bot.message_handler(commands=['viewtasks'])
def view_tasks_command(message):
    if tasks:
        task_list = "\n".join(f"{i + 1}. {task}" for i, task in enumerate(tasks))
        bot.reply_to(message, f"📋 Current Tasks:\n{task_list}")
    else:
        bot.reply_to(message, "No tasks available! Use /addtask to add a new task.")

# Remove Task Command
@bot.message_handler(commands=['removetask'])
def remove_task_command(message):
    task = message.text.replace('/removetask', '').strip()
    if task:
        if task in tasks:
            tasks.remove(task)
            bot.reply_to(message, f"🗑️ Task removed: '{task}'")
        else:
            bot.reply_to(message, "❗ Task not found! Use /viewtasks to see the list of tasks.")
    else:
        bot.reply_to(message, "❗ Usage: /removetask <task> - Please specify the task to remove.")

# Complete Task Command
@bot.message_handler(commands=['completetask'])
def complete_task_command(message):
    task = message.text.replace('/completetask', '').strip()
    if task:
        if task in tasks:
            tasks.remove(task)
            bot.reply_to(message, f"✅ Task completed: '{task}'")
        else:
            bot.reply_to(message, "❗ Task not found! Use /viewtasks to see the list of tasks.")
    else:
        bot.reply_to(message, "❗ Usage: /completetask <task> - Please specify the task to mark as completed.")

# Clear All Tasks Command
@bot.message_handler(commands=['cleartasks'])
def clear_tasks_command(message):
    if tasks:
        tasks.clear()
        bot.reply_to(message, "🧹 All tasks have been cleared!")
    else:
        bot.reply_to(message, "❗ No tasks to clear.")

# Echo Other Messages
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, "I'm here to assist! Use /help to see available commands.")

# Start Polling
bot.polling()
