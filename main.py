import folium
import pandas as pd

# 从CSV文件中读取地震数据
file_path = 'earthquakes_2023_global.csv'
earthquake_data = pd.read_csv(file_path)

# 创建地图，以美国为中心
map_center = [37.7749, -122.4194]  # 旧金山的坐标，可以根据需要调整中心点
my_map = folium.Map(location=map_center, zoom_start=3)

# 在地图上添加地震标记
for index, row in earthquake_data.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=row['mag'] * 2,  # 根据震级调整圆圈的大小
        popup=f"震级: {row['mag']}",
        color='red',
        fill=True,
        fill_color='red'
    ).add_to(my_map)

# 保存地图为 HTML 文件
my_map.save('earthquake_map.html')
