#Step 6 Create Bar Chart Visualization

import matplotlib.pyplot as plt; plt.rcdefaults()

#Set up categories and data 
objects = ('White ('+str(name_counts[0]) + ')', 'Black ('+str(name_counts[1]) + ')', 'Asian/Pacific ('+str(name_counts[2]) + ') ', 'Hispanic/Latino ('+str(name_counts[3]) + ')')
y_pos = np.arange(len(objects))
performance = [name_race_avg['pctwhite'],name_race_avg['pctblack'],name_race_avg['pctapi'],name_race_avg['pcthispanic']]

#Plot data
plt.bar(y_pos, performance, align='center', alpha=2)
plt.xticks(y_pos, objects)
plt.ylabel('Avg Association')
plt.title('Nevative Word Associations by Race/Ethnicity')

fig1 = plt.figure(1, figsize=(9, 6))

fig1.savefig('fig1.png', bbox_inches='tight')


#Step 7 Create Box Plot Visualizations

import matplotlib as mpl
mpl.use('agg')

## Create data
collectn_1 = name_race_raw['pctwhite']
collectn_2 = name_race_raw['pctblack']
collectn_3 = name_race_raw['pctapi']
collectn_4 = name_race_raw['pcthispanic']

## combine these different collections into a list    
data_to_plot = [collectn_1, collectn_2, collectn_3, collectn_4]

# Create a figure instance
fig2 = plt.figure(2, figsize=(9, 6))

# Create an axes instance
ax = fig2.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(data_to_plot)

## add patch_artist=True option to ax.boxplot() 
## to get fill color
bp = ax.boxplot(data_to_plot, patch_artist=True)

## change outline color, fill color and linewidth of the boxes
for box in bp['boxes']:
    # change outline color
    box.set( color='#7570b3', linewidth=2)
    # change fill color
    box.set( facecolor = '#1b9e77' )

## change color and linewidth of the whiskers
for whisker in bp['whiskers']:
    whisker.set(color='#7570b3', linewidth=2)

## change color and linewidth of the caps
for cap in bp['caps']:
    cap.set(color='#7570b3', linewidth=2)

## change color and linewidth of the medians
for median in bp['medians']:
    median.set(color='#b2df8a', linewidth=2)

## change the style of fliers and their fill
for flier in bp['fliers']:
    flier.set(marker='o', color='#e7298a', alpha=0.5)

## Custom x-axis labels
ax.set_xticklabels(['White ('+str(name_counts[0]) + ')', 'Black ('+str(name_counts[1]) + ')', 'Asian/Pacific ('+str(name_counts[2]) + ')', 'Hispanic/Latino ('+str(name_counts[3]) + ')'])

## Remove top axes and right axes ticks
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

plt.title('Nevative Word Associations by Race/Ethnicity')

# Save the figure
fig2.savefig('fig2.png', bbox_inches='tight')


#Step 8 Create Multiple Radar Visualizations
# Set data frame
df = pd.DataFrame({
'group': ['White ('+str(name_counts[0]) + ')', 'Black ('+str(name_counts[1]) + ')', 'Asian/Pacific ('+str(name_counts[2]) + ')', 'Hispanic/Latino ('+str(name_counts[3]) + ')'],
'arrest': [pctwhite_avg['arrest'], pctblack_avg['arrest'], pctapi_avg['arrest'], pcthispanic_avg['arrest']],
'murder': [pctwhite_avg['murder'], pctblack_avg['murder'], pctapi_avg['murder'], pcthispanic_avg['murder']],
'homicide': [pctwhite_avg['homicide'], pctblack_avg['homicide'], pctapi_avg['homicide'], pcthispanic_avg['homicide']],
'crime': [pctwhite_avg['crime'], pctblack_avg['crime'], pctapi_avg['crime'], pcthispanic_avg['crime']],
'prison': [pctwhite_avg['prison'], pctblack_avg['prison'], pctapi_avg['prison'], pcthispanic_avg['prison']]
})

# number of variables
categories=list(df)[:2]
categories+=list(df)[3:]
N = len(categories)

def make_spider(row, title, color):
     
    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
     
    # Initialise the spider plot
    ax = plt.subplot(2,2,row+1, polar=True, )
     
    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
     
    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=8)
     
    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([2,4,6,8], ["2","4","6","8"], color="grey", size=7)
    plt.ylim(0,10)
     
    # Ind1
    values=df.loc[row].drop('group').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, color=color, linewidth=2, linestyle='solid')
    ax.fill(angles, values, color=color, alpha=0.4)
     
    # Add a title
    plt.title(title, size=11, color=color, y=1.1)

# ------- PART 2: Apply to all individuals
# initialize the figure
my_dpi=300
fig3 = plt.figure(figsize=(3000/my_dpi, 3300/my_dpi), dpi=my_dpi)
 
# Create a color palette:
my_palette = plt.cm.get_cmap("Set2", len(df.index))
 
# Loop to plot
for row in range(0, len(df.index)):
    make_spider( row=row, title=df['group'][row], color=my_palette(row))

fig3.savefig('fig3.png', bbox_inches='tight')


#Step 9 Create Joint Radar Visualization

# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
# Initialise the spider plot
ax = plt.subplot(111, polar=True)
 
# If you want the first axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
 
# Draw one axe per variable + add labels labels yet
plt.xticks(angles[:-1], categories)
 
# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([2,4,6,8], ["2","4","6","8"], color="grey", size=7)
plt.ylim(0,10)


 
# ------- PART 2: Add plots
 
# Plot each individual = each line of the data
# I don't do a loop, because plotting more than 3 groups makes the chart unreadable

my_palette = plt.cm.get_cmap("Set2", len(df.index))
    
for i in range(0,len(df.index)):
    values=df.loc[i].drop('group').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, color=my_palette(i), linewidth=1, linestyle='solid', label="group A")
    ax.fill(angles, values, color=my_palette(i), alpha=0.1)

plt.title("Negative word assotiations by name and race \n")

plt.savefig('fig4.png')

