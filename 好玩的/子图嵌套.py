import matplotlib.patches as mpatches
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter,LatitudeFormatter
import matplotlib.ticker as ticker
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.colors
import cmaps

path='E:\\浏览器下载\\ETOPO2v2c_f4_netCDF (2)\\ETOPO2v2c_f4_netCDF\\ETOPO2v2c_f4.nc'
data = xr.open_dataset(path).sel(y=slice(0,35),
                                x=slice(118,125))
lon = data.x.data
lat = data.y.data


colors_below = cmaps.cmocean_algae(np.linspace(0, 1, 256))[::1]
colors_upper = cmaps.MPL_Blues(np.linspace(0, 1, 256))[::-1]

# 合并颜色数组
colors = np.vstack((colors_upper,colors_below, ))

# 创建新的颜色映射
cmaps = mcolors.LinearSegmentedColormap.from_list('custom_cmap', colors)


norm = mcolors.Normalize(vmin=-2000, vmax=2000)

box   = [120.5,123,30.5,32.5]
xtick = np.arange(box[0], box[1]+0.1, 0.5)
ytick = np.arange(box[2], box[3]+0.1, 0.5)

plt.rcParams['font.sans-serif'] = ['Times New Roman']


#############################################################################################################################

# Create figure and axes
fig = plt.figure(figsize=(10, 8), dpi=300)
proj = ccrs.PlateCarree()

# Main subplot
ax = fig.add_axes([0, 0.5, 0.8, 0.8], projection=proj)
ax.set_extent([120.5, 123, 30.5, 32], crs=ccrs.PlateCarree())
ax.add_feature(cfeature.LAKES.with_scale('10m'), color='lightskyblue', alpha=.99)
ax.add_feature(cfeature.RIVERS.with_scale('10m'))
ax.add_feature(cfeature.OCEAN.with_scale('10m'))
ax.add_feature(cfeature.LAND.with_scale('10m'))
cf = ax.contourf(lon, lat, data['z'], norm=norm,
                 levels=np.arange(-2000, 2001, 50),
                 transform=ccrs.PlateCarree(),
                 cmap=cmaps, extend='neither')
cbar = fig.colorbar(cf, ax=ax, label='Global Elevation (meter)',shrink=0.55,
                    format=ticker.ScalarFormatter(useMathText=True))
cbar.ax.tick_params(which='major', direction='in')

# Scatter points
points = [(121.84, 31.3), (121.47, 31.23), (121.65, 31.86), (120.75, 30.75)]
for point in points:
    ax.scatter(point[0], point[1], transform=ccrs.PlateCarree(), marker='o',
               alpha=0.8, s=100, edgecolor='black', color='r' if point[0] == 121.84 else 'w')

# Annotations

ax.annotate('Shanghai', (121.47, 31.26))
ax.annotate('Qidong', (121.65, 31.89))
ax.annotate('Jiaxing', (120.75, 30.79))

# Gridlines and ticks
xtick = np.arange(120.5, 123.1, 0.5)
ytick = np.arange(30.5, 32.1, 0.5)
tick_proj = ccrs.PlateCarree()
ax.set_xticks(xtick, crs=tick_proj)
ax.set_yticks(ytick, crs=tick_proj)
ax.gridlines(linestyle='--', xlocs=xtick, ylocs=ytick, zorder=2, linewidth=0.5, color='grey')

# Arrow and labels
arrow_x, arrow_y, arrow_length = 0.94, 0.86, 0.05
ax.arrow(arrow_x, arrow_y, 0, arrow_length, transform=ax.transAxes,
         color='black', width=0.001, head_width=0.01, head_length=0.03)

ax.text(122.7, 31.5, 'East sea', ha='right', va='center', fontsize=18, transform=ccrs.PlateCarree())
ax.tick_params(which='major', direction='in',pad=8)
# Zoomed-in subplot
ax.xaxis.set_major_formatter(LongitudeFormatter(zero_direction_label =False))
ax.yaxis.set_major_formatter(LatitudeFormatter())

ax2 = fig.add_axes([0.33, 0.22, 0.4, 0.4], projection=proj)
ax2.set_extent([121.5, 122, 31, 31.5], crs=ccrs.PlateCarree())
ax2.add_feature(cfeature.LAKES.with_scale('10m'), color='lightskyblue', alpha=.99)
ax2.add_feature(cfeature.RIVERS.with_scale('10m'))
ax2.add_feature(cfeature.OCEAN.with_scale('10m'))
ax2.add_feature(cfeature.LAND.with_scale('10m'))
cf_zoomed = ax2.contourf(lon, lat, data['z'], levels=np.arange(-2000, 2001, 50),
                          transform=ccrs.PlateCarree(), cmap=cmaps, extend='neither')
ax.plot([121.5,122,122,121.5,121.5],[31,31,31.5,31.5,31],lw=1,transform=ccrs.PlateCarree(),
        color='tab:red')
xtick2 = np.arange(121.5, 122.1, 0.1)
ytick2 = np.arange(31, 31.6, 0.2)
ax2.set_xticks(xtick2, crs=tick_proj)
ax2.set_yticks(ytick2, crs=tick_proj)
ax2.gridlines(linestyle='--', xlocs=[121.5,121.6,121.7,121.8,121.9], ylocs=[31,31.2,31.4,31.6], zorder=2, linewidth=0.5, color='grey')

line_x = [121.5, 122, 122, 121.5, 121.5]
line_y = [31, 31, 31.5, 31.5, 31]

line = mpatches.ConnectionPatch((line_x[0], line_y[0]), (line_x[0], line_y[1]),
                            coordsA=ax.transData, coordsB=ax2.transData,
                            color='tab:red'
                                )
ax2.add_patch(line)

line1 = mpatches.ConnectionPatch((line_x[1], line_y[2]), (line_x[1], 31.6),
                            coordsA=ax.transData, coordsB=ax2.transData,
                            color='tab:red'
                                )
ax2.add_patch(line1)

ax2.annotate('HSD', (121.85, 31.3), xytext=(5, -10), textcoords='offset points',
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.9'))

ax2.scatter(121.84, 31.30, transform=ccrs.PlateCarree(), marker='o',
           alpha=0.8, s=100, edgecolor='black', color='r' )

ax2.xaxis.set_major_formatter(LongitudeFormatter(zero_direction_label =False))
ax2.yaxis.set_major_formatter(LatitudeFormatter())
ax2.tick_params(which='major', direction='in',pad=8)
plt.show()
