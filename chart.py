import matplotlib.pyplot as plt

fig, ax = plt.subplots()

languages = ['Python', 'Java', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
bar_colors = ['blue', 'red', 'green', 'yellow', 'purple', 'orange']

ax.bar(languages, popularity, color=bar_colors)

ax.set_title('Popularity of Programming Languages')
ax.set_xlabel('Languages')
ax.set_ylabel('Popularity (%)')
ax.legend(title='Popularity', loc='upper right')

plt.show()

# pie chart
fig2, ax = plt.subplots()
ax.pie(popularity, labels=languages, autopct='%1.1f%%', shadow={'ox': -0.04, 'edgecolor': 'none', 'shade': 0.9},  startangle=90)
plt.show()