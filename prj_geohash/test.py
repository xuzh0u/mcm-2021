#!/usr/bin/python 
# -*- coding:utf-8 -*-
# author: zheng
# datetime: 2021/2/6 21:56
# software: PyCharm

from pygeohash import encode, decode
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import math
from matplotlib.path import Path


def getMainMap():
    """
    作用：获取广州各个分界点的编码、经、纬度子集、经纬度最值；
    :return:
    """
    # 广州的边界，三维列表；
    G = [[[114.03621, 23.90178], [114.04083, 23.8735], [114.05776, 23.84676], [114.05227, 23.83003],
          [114.03699, 23.81871], [114.03761, 23.80803], [114.04775, 23.80334], [114.03678, 23.79563],
          [114.05996, 23.77587], [114.03845, 23.77122], [114.02312, 23.75224], [114.01821, 23.76284],
          [114.00995, 23.76301], [114.01313, 23.77795], [113.99879, 23.76301], [113.97611, 23.75772],
          [113.97286, 23.73925], [113.92005, 23.72945], [113.91236, 23.71651], [113.90094, 23.71543],
          [113.88731, 23.6881], [113.84784, 23.67933], [113.85276, 23.66777], [113.84392, 23.66948],
          [113.83995, 23.65545], [113.81878, 23.65617], [113.82837, 23.64592], [113.81377, 23.62901],
          [113.85962, 23.60997], [113.86405, 23.58739], [113.85282, 23.57058], [113.86314, 23.56536],
          [113.87138, 23.54131], [113.88814, 23.53507], [113.89234, 23.52111], [113.91152, 23.50416],
          [113.94625, 23.49319], [113.93298, 23.47971], [113.97412, 23.47882], [113.98171, 23.47215],
          [113.97449, 23.4649], [113.95412, 23.46563], [113.95281, 23.44289], [113.96191, 23.43141],
          [113.98707, 23.43168], [113.98428, 23.40848], [113.99986, 23.39664], [113.98119, 23.37765],
          [114.00153, 23.34472], [113.99391, 23.33316], [113.98361, 23.33258], [113.9967, 23.29746],
          [113.95847, 23.31495], [113.95969, 23.33147], [113.93927, 23.34295], [113.89599, 23.34507],
          [113.8892, 23.33357], [113.89821, 23.32055], [113.89028, 23.28269], [113.87659, 23.26498],
          [113.89516, 23.25355], [113.89011, 23.24213], [113.90377, 23.21254], [113.894, 23.21266],
          [113.8838, 23.19169], [113.88898, 23.17863], [113.90229, 23.17326], [113.89146, 23.16325],
          [113.87478, 23.16535], [113.85873, 23.15725], [113.84897, 23.14772], [113.84108, 23.11615],
          [113.81467, 23.12777], [113.75405, 23.12957], [113.7386, 23.14131], [113.72437, 23.14122],
          [113.68781, 23.1198], [113.66115, 23.11142], [113.66043, 23.11877], [113.65125, 23.1193],
          [113.64028, 23.10389], [113.6104, 23.10379], [113.58642, 23.0878], [113.55629, 23.08124],
          [113.52289, 23.03727], [113.52923, 22.98261], [113.57428, 22.89194], [113.57122, 22.85312],
          [113.68528, 22.71773], [113.71686, 22.6452], [113.73762, 22.52766], [113.70598, 22.51629],
          [113.65161, 22.51572], [113.62078, 22.57953], [113.56163, 22.60751], [113.53297, 22.65498],
          [113.54072, 22.66621], [113.47131, 22.71499], [113.46797, 22.72852], [113.41219, 22.74283],
          [113.36351, 22.77412], [113.35654, 22.79297], [113.37468, 22.79456], [113.39343, 22.80985],
          [113.37442, 22.8226], [113.34652, 22.81614], [113.3121, 22.83039], [113.30966, 22.85119],
          [113.29614, 22.85991], [113.30083, 22.87677], [113.27703, 22.8947], [113.28596, 22.90144],
          [113.2824, 22.92739], [113.2981, 22.93431], [113.28632, 22.95032], [113.26705, 22.95494],
          [113.24993, 22.97329], [113.2579, 22.99486], [113.24966, 23.00204], [113.25286, 23.01977],
          [113.26313, 23.02114], [113.2578, 23.04677], [113.21169, 23.04332], [113.17792, 23.06803],
          [113.17741, 23.07756], [113.20907, 23.08346], [113.21673, 23.09866], [113.20814, 23.09968],
          [113.20247, 23.12111], [113.21055, 23.12337], [113.21267, 23.1411], [113.18686, 23.14825],
          [113.1896, 23.16195], [113.20945, 23.1771], [113.209, 23.19218], [113.17748, 23.22088], [113.182, 23.25278],
          [113.17653, 23.2736], [113.12798, 23.31455], [113.12437, 23.30659], [113.11322, 23.30986],
          [113.10575, 23.30273], [113.10568, 23.29027], [113.07164, 23.28371], [113.08083, 23.25087],
          [113.04476, 23.25096], [113.05378, 23.26378], [113.05143, 23.27839], [113.03263, 23.29767],
          [113.03755, 23.32007], [113.02347, 23.3249], [113.04309, 23.353], [113.03354, 23.35682],
          [113.01671, 23.34093], [113.01169, 23.35358], [112.98798, 23.35588], [112.98103, 23.38142],
          [112.98632, 23.39863], [113.00109, 23.40633], [112.98165, 23.43297], [112.98911, 23.4433],
          [112.96339, 23.42642], [112.95922, 23.43539], [112.97928, 23.46515], [113.01594, 23.46058],
          [113.02636, 23.47286], [113.05585, 23.47196], [113.08374, 23.4945], [113.11545, 23.50151],
          [113.1161, 23.51074], [113.15354, 23.50284], [113.1711, 23.51156], [113.17232, 23.52029],
          [113.1721, 23.51237], [113.19206, 23.51477], [113.19112, 23.52321], [113.21268, 23.54028],
          [113.20078, 23.56183], [113.20224, 23.57652], [113.22698, 23.58574], [113.22789, 23.59442],
          [113.24441, 23.58688], [113.24038, 23.60624], [113.24847, 23.60159], [113.27657, 23.616],
          [113.28134, 23.60836], [113.29946, 23.63689], [113.28927, 23.64436], [113.32726, 23.64442],
          [113.32796, 23.65548], [113.34908, 23.66797], [113.36372, 23.70716], [113.37539, 23.71282],
          [113.37836, 23.73153], [113.40431, 23.7235], [113.44191, 23.72704], [113.44386, 23.71592],
          [113.4643, 23.70797], [113.46871, 23.69099], [113.48103, 23.68404], [113.5137, 23.68209],
          [113.54547, 23.69639], [113.53836, 23.6991], [113.54291, 23.70181], [113.55876, 23.70069],
          [113.56805, 23.67944], [113.58729, 23.67523], [113.59835, 23.66267], [113.62259, 23.69944],
          [113.63819, 23.70457], [113.62812, 23.71171], [113.6364, 23.75024], [113.61546, 23.78739],
          [113.65167, 23.82013], [113.68139, 23.81202], [113.68737, 23.82572], [113.70638, 23.81527],
          [113.71855, 23.82076], [113.71353, 23.8625], [113.72476, 23.85356], [113.75817, 23.85749],
          [113.78761, 23.90246], [113.80945, 23.90061], [113.87532, 23.93047], [113.88583, 23.92366],
          [113.89252, 23.93167], [113.91024, 23.92357], [113.93353, 23.92923], [113.94117, 23.92357],
          [113.96945, 23.93256], [113.98452, 23.92617], [114.00921, 23.93291], [114.03294, 23.92039],
          [114.03621, 23.90178]]]
    # 得到广州边界的分区情况和经纬度集合；
    p, lon, lat = Partition(G)
    lonmax = np.max((lon))  # 经度最大值：
    lonmin = np.min((lon))  # 经度最大值：
    latmax = np.max((lat))  # 维度最大值：
    latmin = np.min((lat))  # 经度最大值：
    return lonmax, lonmin, latmax, latmin, p, lon, lat


def Partition(G):
    """
    :param G: 广州边界坐标集合，形式为三维数组。
    :return:
    """
    lon = []
    lat = []
    p = []
    for i in range(len(G)):
        for j in range(len(G[i])):
            lat.append(G[i][j][1])
            lon.append(G[i][j][0])
            result = get_geohash(G[i][j][1], G[i][j][0])
            p.append(result)
    return p, lon, lat


def get_geohash(lon, lat):
    # 获取大致分区：
    geo = encode(lon, lat)
    return geo


# 获取解码：输入为编码，输出为解码
def get_lonlat(geo):
    # 获取大致分区：
    lon, lat = decode(geo)
    return lon, lat


def get_totalgeohash():
    # 获取最值
    lonmax, lonmin, latmax, latmin, p, lon, lat = getMainMap()
    # 枚举划分：
    accu = 0.01
    total = []
    total_lon = []
    total_lat = []
    # 存储所有划分的出来的区域的编码
    for i in np.arange(latmin, latmax, accu):
        for j in np.arange(lonmin, lonmax, accu):
            total.append(get_geohash(i, j))
            a, b = get_lonlat(get_geohash(i, j))
            # 纬度
            total_lat.append(a)
            # 经度
            total_lon.append(b)
    return total, p, lon, lat


def get_geolonlat_zt(total):
    new_total = []  # 全部的多级编码
    block_dict = {}
    central_dict = {}
    for i in total:  # 得到的前n位全部的编码
        new_total.append(i[:5])  # 只能取4个
    new_total = list(set(new_total))  # 得到编码的个数
    new_total_lonlat = []
    for block in new_total:
        lat_zt, lon_zt = get_lonlat(block)
        new_total_lonlat.append([lon_zt, lat_zt])
    return new_total_lonlat


def match_zt(total):
    new_total_lonlat = get_geolonlat_zt(total)
    all_centralpoint = new_total_lonlat
    new_total_lon = []
    new_total_lat = []
    for point in all_centralpoint:
        new_total_lon.append(point[0])
        new_total_lat.append(point[1])
    return all_centralpoint, new_total_lon, new_total_lat


def border_point_zt(lon, lat):
    line_lon = list(set(lon[:]))  # 画出分区点的经度
    line_lat = list(set(lat[:]))  # 画出分区点的纬度
    aver_lons = []
    aver_lats = []
    line_lon.sort()
    line_lat.sort()
    # print(len(line_lon))
    for i in range(len(line_lon) - 1):
        aver_lons.append((line_lon[i] + line_lon[i + 1]) / 2)
    # input(len(aver_lons))
    subtract_lon = abs(line_lon[0] - line_lon[1]) / 2
    # 加上左边界
    aver_lons.insert(0, line_lon[0] - subtract_lon)
    # 加上右边界
    aver_lons.append(line_lon[len(line_lon) - 1] + subtract_lon)
    # 同理
    for i in range(len(line_lat) - 1):
        aver_lats.append((line_lat[i] + line_lat[i + 1]) / 2)
    subtract_lat = abs(line_lat[0] - line_lat[1]) / 2
    aver_lats.insert(0, line_lat[0] - subtract_lat)
    aver_lats.append(line_lat[len(line_lat) - 1] + subtract_lat)
    # print(aver_lons, aver_lats)
    aver_lats.sort()
    aver_lons.sort()
    return aver_lons, aver_lats


def get_dict(central_points, aver_lons, aver_lats):
    point_dict = {}
    lon_var = (aver_lons[1] - aver_lons[0]) / 2
    lat_var = (aver_lats[1] - aver_lats[0]) / 2
    for central_point in central_points:
        border_points = []
        lons = [central_point[0] + lon_var, central_point[0] - lon_var]
        lats = [central_point[1] + lat_var, central_point[1] - lat_var]
        for lon in lons:
            for lat in lats:
                border_points.append([lon, lat])
        point_dict[str(central_point)] = border_points
    return point_dict


def match(dict):
    p = edge_info()
    match_point1 = []
    match_point2 = []
    new_dict = {}
    # 遍历每一个键
    for key in dict.keys():
        flag = 0
        # 遍历一个键对应的每一个坐标
        for i in dict[key]:
            if p.contains_points([tuple(i)]) == [True]:
                # 为 0 时不满足
                flag = 1
        if flag == 1:
            a = key[1:-1].split(",")
            for k in range(len(a)):
                a[k] = float(a[k])
            match_point1.append(a)
            for j in dict[key]:
                match_point2.append(j)
            new_dict[str(a)] = dict[key]
    return match_point1, match_point2, new_dict


def edge_info():
    G = [[[114.03621, 23.90178], [114.04083, 23.8735], [114.05776, 23.84676], [114.05227, 23.83003],
          [114.03699, 23.81871],
          [114.03761, 23.80803], [114.04775, 23.80334], [114.03678, 23.79563], [114.05996, 23.77587],
          [114.03845, 23.77122],
          [114.02312, 23.75224], [114.01821, 23.76284], [114.00995, 23.76301], [114.01313, 23.77795],
          [113.99879, 23.76301],
          [113.97611, 23.75772], [113.97286, 23.73925], [113.92005, 23.72945], [113.91236, 23.71651],
          [113.90094, 23.71543],
          [113.88731, 23.6881], [113.84784, 23.67933], [113.85276, 23.66777], [113.84392, 23.66948],
          [113.83995, 23.65545],
          [113.81878, 23.65617], [113.82837, 23.64592], [113.81377, 23.62901], [113.85962, 23.60997],
          [113.86405, 23.58739],
          [113.85282, 23.57058], [113.86314, 23.56536], [113.87138, 23.54131], [113.88814, 23.53507],
          [113.89234, 23.52111],
          [113.91152, 23.50416], [113.94625, 23.49319], [113.93298, 23.47971], [113.97412, 23.47882],
          [113.98171, 23.47215],
          [113.97449, 23.4649], [113.95412, 23.46563], [113.95281, 23.44289], [113.96191, 23.43141],
          [113.98707, 23.43168],
          [113.98428, 23.40848], [113.99986, 23.39664], [113.98119, 23.37765], [114.00153, 23.34472],
          [113.99391, 23.33316],
          [113.98361, 23.33258], [113.9967, 23.29746], [113.95847, 23.31495], [113.95969, 23.33147],
          [113.93927, 23.34295],
          [113.89599, 23.34507], [113.8892, 23.33357], [113.89821, 23.32055], [113.89028, 23.28269],
          [113.87659, 23.26498],
          [113.89516, 23.25355], [113.89011, 23.24213], [113.90377, 23.21254], [113.894, 23.21266],
          [113.8838, 23.19169],
          [113.88898, 23.17863], [113.90229, 23.17326], [113.89146, 23.16325], [113.87478, 23.16535],
          [113.85873, 23.15725],
          [113.84897, 23.14772], [113.84108, 23.11615], [113.81467, 23.12777], [113.75405, 23.12957],
          [113.7386, 23.14131],
          [113.72437, 23.14122], [113.68781, 23.1198], [113.66115, 23.11142], [113.66043, 23.11877],
          [113.65125, 23.1193],
          [113.64028, 23.10389], [113.6104, 23.10379], [113.58642, 23.0878], [113.55629, 23.08124],
          [113.52289, 23.03727],
          [113.52923, 22.98261], [113.57428, 22.89194], [113.57122, 22.85312], [113.68528, 22.71773],
          [113.71686, 22.6452],
          [113.73762, 22.52766], [113.70598, 22.51629], [113.65161, 22.51572], [113.62078, 22.57953],
          [113.56163, 22.60751],
          [113.53297, 22.65498], [113.54072, 22.66621], [113.47131, 22.71499], [113.46797, 22.72852],
          [113.41219, 22.74283],
          [113.36351, 22.77412], [113.35654, 22.79297], [113.37468, 22.79456], [113.39343, 22.80985],
          [113.37442, 22.8226],
          [113.34652, 22.81614], [113.3121, 22.83039], [113.30966, 22.85119], [113.29614, 22.85991],
          [113.30083, 22.87677],
          [113.27703, 22.8947], [113.28596, 22.90144], [113.2824, 22.92739], [113.2981, 22.93431],
          [113.28632, 22.95032],
          [113.26705, 22.95494], [113.24993, 22.97329], [113.2579, 22.99486], [113.24966, 23.00204],
          [113.25286, 23.01977],
          [113.26313, 23.02114], [113.2578, 23.04677], [113.21169, 23.04332], [113.17792, 23.06803],
          [113.17741, 23.07756],
          [113.20907, 23.08346], [113.21673, 23.09866], [113.20814, 23.09968], [113.20247, 23.12111],
          [113.21055, 23.12337],
          [113.21267, 23.1411], [113.18686, 23.14825], [113.1896, 23.16195], [113.20945, 23.1771], [113.209, 23.19218],
          [113.17748, 23.22088], [113.182, 23.25278], [113.17653, 23.2736], [113.12798, 23.31455],
          [113.12437, 23.30659],
          [113.11322, 23.30986], [113.10575, 23.30273], [113.10568, 23.29027], [113.07164, 23.28371],
          [113.08083, 23.25087],
          [113.04476, 23.25096], [113.05378, 23.26378], [113.05143, 23.27839], [113.03263, 23.29767],
          [113.03755, 23.32007],
          [113.02347, 23.3249], [113.04309, 23.353], [113.03354, 23.35682], [113.01671, 23.34093],
          [113.01169, 23.35358],
          [112.98798, 23.35588], [112.98103, 23.38142], [112.98632, 23.39863], [113.00109, 23.40633],
          [112.98165, 23.43297],
          [112.98911, 23.4433], [112.96339, 23.42642], [112.95922, 23.43539], [112.97928, 23.46515],
          [113.01594, 23.46058],
          [113.02636, 23.47286], [113.05585, 23.47196], [113.08374, 23.4945], [113.11545, 23.50151],
          [113.1161, 23.51074],
          [113.15354, 23.50284], [113.1711, 23.51156], [113.17232, 23.52029], [113.1721, 23.51237],
          [113.19206, 23.51477],
          [113.19112, 23.52321], [113.21268, 23.54028], [113.20078, 23.56183], [113.20224, 23.57652],
          [113.22698, 23.58574],
          [113.22789, 23.59442], [113.24441, 23.58688], [113.24038, 23.60624], [113.24847, 23.60159],
          [113.27657, 23.616],
          [113.28134, 23.60836], [113.29946, 23.63689], [113.28927, 23.64436], [113.32726, 23.64442],
          [113.32796, 23.65548],
          [113.34908, 23.66797], [113.36372, 23.70716], [113.37539, 23.71282], [113.37836, 23.73153],
          [113.40431, 23.7235],
          [113.44191, 23.72704], [113.44386, 23.71592], [113.4643, 23.70797], [113.46871, 23.69099],
          [113.48103, 23.68404],
          [113.5137, 23.68209], [113.54547, 23.69639], [113.53836, 23.6991], [113.54291, 23.70181],
          [113.55876, 23.70069],
          [113.56805, 23.67944], [113.58729, 23.67523], [113.59835, 23.66267], [113.62259, 23.69944],
          [113.63819, 23.70457],
          [113.62812, 23.71171], [113.6364, 23.75024], [113.61546, 23.78739], [113.65167, 23.82013],
          [113.68139, 23.81202],
          [113.68737, 23.82572], [113.70638, 23.81527], [113.71855, 23.82076], [113.71353, 23.8625],
          [113.72476, 23.85356],
          [113.75817, 23.85749], [113.78761, 23.90246], [113.80945, 23.90061], [113.87532, 23.93047],
          [113.88583, 23.92366],
          [113.89252, 23.93167], [113.91024, 23.92357], [113.93353, 23.92923], [113.94117, 23.92357],
          [113.96945, 23.93256],
          [113.98452, 23.92617], [114.00921, 23.93291], [114.03294, 23.92039], [114.03621, 23.90178]]]
    # 交换位置,并转化形式：
    a = []
    for i in G[0]:
        a.append(tuple(i))
    p = Path(a)
    return p


# 画图
def geo_paint_new(central_points, border_points, geo1, lon1, lat1, new_dict):
    central_points_lon = [];
    central_points_lat = []
    border_points_lon = [];
    border_points_lat = []
    for central_point in central_points:  # 得到中心点的经纬度
        central_points_lon.append(central_point[0])
        central_points_lat.append(central_point[1])
    # border_points = list(set(border_points))
    border_points1 = list(set([tuple(border_point) for border_point in border_points]))
    border_points = []

    central_points_lon = pd.DataFrame(central_points_lon)
    central_points_lat = pd.DataFrame(central_points_lat)
    datas = [  # 画出边界点以及每一个中心点的位置
        go.Scattermapbox(
            lat=lat1,
            lon=lon1,
            text=geo1,
            mode='markers',
            hoverinfo='text',
            marker=go.scattermapbox.Marker(
                size=5,
                color='#000045',
                opacity=0.3
            )
        ),
        go.Scattermapbox(
            lat=central_points_lat,
            lon=central_points_lon,
            # text=geo,
            mode='markers',
            # hoverinfo='text',
            marker=go.scattermapbox.Marker(
                size=5,
                color='#de9dac',  # 000045
                opacity=0.8
            )
        )
    ]
    for key in new_dict.keys():
        borders = new_dict[key]
        lons = [];
        lats = []
        for border in borders:
            lons.append(border[0])
            lats.append(border[1])
        lons1 = list(set(lons))
        lats1 = list(set(lats))
        lats1.sort()
        lons1.sort()
        lons = [lons1[0], lons1[0], lons1[1], lons1[1], lons1[0]]
        lats = [lats1[0], lats1[1], lats1[1], lats1[0], lats1[0]]
        lons = pd.DataFrame(lons)
        lats = pd.DataFrame(lats)
        datas.append(
            go.Scattermapbox(
                lat=lats,
                lon=lons,
                # text=geo,
                mode='markers+lines',
                # hoverinfo='text',
                marker=go.scattermapbox.Marker(
                    size=5,
                    color='green',  # 000045
                    opacity=0.8
                )
            )
        )
    mapbox_access_token = 'pk.eyJ1IjoiY2h1YW4tMzI1IiwiYSI6ImNra3RzczRsYjEwcXMzMHJ0MHFpa25nazkifQ.s-z4MzS4cTVChGuivvE4KA'
    layout = go.layout(
        title="Guangzhou_geo",
        autosize=True,
        hovermode='closest',
        showlegend=False,
        mapbox=go.layout.mapbox(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=go.layout.mapbox.Center(
                lat=23.12864583,  # 广州市纬度
                lon=113.2648325  # 广州市经度
            ),
            pitch=0,
            zoom=10,
            style='light'
        ),
    )

    fig = go.Figure(data=datas, layout=layout)
    py.plot(fig, filename='Guangzhou_geo.html')  # 生成html文件并打开


if __name__ == "__main__":
    total, p, lon, lat = get_totalgeohash()  # 得到全部的编码， 边界的各个信息
    central_point, new_total_lon, new_total_lat = match_zt(total)
    aver_lons, aver_lats = border_point_zt(new_total_lon, new_total_lat)
    point_dict = get_dict(central_point, aver_lons, aver_lats)
    central_points, border_points, new_dict = match(point_dict)
    geo_paint_new(central_points, border_points, p, lon, lat, new_dict)
