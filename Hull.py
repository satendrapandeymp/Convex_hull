import numpy as np

def tan_cal(cir1, cir2, spec):
	tana = (cir2["y"] - cir1["y"]) / (cir2["x"] -  cir1["x"])
	dist = ((cir2["y"] - cir1["y"])**2 + (cir2["x"] -  cir1["x"])**2 )**.5
	tanb = spec * (cir2["r"]-cir1["r"]) / dist
	tan = (tana + tanb)/(1 - tana * tanb)
	return tan

def ups(x,y,x1,y1,x2,y2):
	y_p = ((y1-y2)/(x1-x2)) * (x-x1) + y1
	if (y-y_p) > 0:
		return 1
	return 0	

def hull(arr, spec):
	result = []
	count = 0
	index = 100000
	total = len(arr)
	while(count < total):
		if count == 0:
			result.append(count)
		else:
			tan = spec * tan_cal(arr[count-1], arr[count], spec)
			if tan >= index:
				result = result[:-1]
				result.append(count)
				index = tan
			else:
				result.append(count)
				index = tan
	
		count += 1
	
	return result	

def find_hull(points):
	pos = []
	neg = []

	for point in points:
		if ups(point["x"], point["y"], points[0]["x"], points[0]["y"], points[-1]["x"], points[-1]["y"]) == 0:
			neg.append(point)	
		else:
			pos.append(point)

	# including extreme points
	pos1 = [points[0]]
	pos.append(points[-1])
	pos1 += pos
	pos = pos1

	last = 0
	while(len(pos) != last):
		last = len(pos)		
		arr = hull(pos, 1)
		num = len(arr)
		pos1 = pos
		pos = []
		for i in arr:
			pos.append(pos1[i])

	res = []
	res += pos

	pos = neg
	last = 0
	while(len(pos) != last):
		last = len(pos)		
		arr = hull(pos, -1)
		num = len(arr)
		pos1 = pos
		pos = []
		for i in arr:
			pos.append(pos1[i])
	
	res += pos[1:-1]
	result = []

	for point in res:
		count = 0
		for i in points:
			if point == i:
				break
			else:
				count += 1
		result.append(count)
	
	result.sort()
	return result


if __name__ == "__main__":
	x = np.random.uniform(-4,4,20)
	y = np.random.uniform(-4,4,20)
	r = np.random.uniform(.3,1.2,20)

	points = []

	for i in range(20):
		temp = {"x":x[i],"y":y[i], "r":r[i]}
		points.append(temp)

	points = sorted(points, key = lambda x:(x["x"]-x["r"]))

	count = 0
	for loc in points:
		print loc["x"], loc["y"], loc["r"], count
		count += 1

	result = find_hull(points)
	result.sort()

	print result
