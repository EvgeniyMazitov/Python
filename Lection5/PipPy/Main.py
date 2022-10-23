from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token(
    "5475094735:AAEegquDfOK_KfEckWOU45uFtesfa6Yk4kQ").build()

app.add_handler(CommandHandler("hello", hello))
print('server start')
app.run_polling('server start')


# import matplotlib.pyplot as plt
# import numpy as np

# list = [1, 2, 3, 2, 7]
# plt.plot(list)
# plt.show()
# Fixing random state for reproducibility
# np.random.seed(19680801)


# plt.rcdefaults()
# fig, ax = plt.subplots()

# # Example data
# people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# y_pos = np.arange(len(people))
# performance = 3 + 10 * np.random.rand(len(people))
# error = np.random.rand(len(people))

# ax.barh(y_pos, performance, xerr=error, align='center')
# ax.set_yticks(y_pos, labels=people)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Performance')
# ax.set_title('How fast do you want to go today?')

# plt.show()

# import emoji

# print(emoji.emojize('Python is :thumbsup:', language='alias'))

# import time
# from progress.bar import Bar
# from isOdd import isOdd

# print(isOdd(1))
# print(isOdd(4))

# bar = Bar('Processing', max=20)
# for i in range(20):
#     # Do some work
#     time.sleep(1)
#     bar.next()
# bar.finish()
