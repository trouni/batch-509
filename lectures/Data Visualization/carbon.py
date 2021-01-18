import matplotlib.pyplot as plt

years_x = [1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015]
total_y = [1243, 1543, 1619, 1831, 1960, 2310, 2415, 2270, 1918]

coal_y = [823, 1136, 1367, 1547, 1660, 1927, 1983, 1827, 1352]
gas_y = [171, 200, 166, 175, 228, 280, 319, 399, 529]


# plt.style.use('bmh')

plt.plot(years_x, total_y, label="Total")
# plt.savefig('carbon.png')

plt.title("USA - CO2 emissions from electricity production")
plt.xlabel("Year")
plt.ylabel("CO2 - M of tons")

# plt.xticks([1975, 1995, 2015], ['start', 1995, 'end'])
# plt.yticks([0, 3000])

# plt.xlim(2000, 2015)

plt.plot(years_x, coal_y, label="Coal", linestyle=':', marker='X', markerfacecolor="tab:blue", markeredgecolor="tab:blue")
plt.plot(years_x, gas_y, label="Gas")

plt.grid(axis="y",color='#d111d1', linestyle='--', linewidth=0.6)


plt.legend()

ax = plt.gca()
ax.spines['top'].set_color(None)
ax.spines['bottom'].set_position(('axes', 0.5)) # half of y-axis

plt.show()