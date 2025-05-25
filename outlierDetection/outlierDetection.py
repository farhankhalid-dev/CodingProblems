#!/usr/bin/env python3

"""
source: Prob and Stats - Spring 2025
problem: Outlier detection, cleaning dataset, visualization of data
type: Easy
site: None
submission: Moodle
"""


import math 
import matplotlib.pyplot as plt

class Solution():
    def solution(self, dataSet):
        cleanData = self.cleanOutliers(dataSet)
        groupedData = self.groupData(cleanData)
        return groupedData

    def cleanOutliers(self, dataSet):
        dataSet.sort()
        size = len(dataSet)

        q1 = (1/4) * (size + 1)
        q3 = (3/4) * (size + 1)

        q1Floor = int(math.floor(q1))
        q3Floor = int(math.floor(q3))

        q1Frac = q1 - q1Floor
        q3Frac = q3 - q3Floor

        q1Val = dataSet[q1Floor - 1] + q1Frac * (dataSet[q1Floor] - dataSet[q1Floor - 1])
        q3Val = dataSet[q3Floor - 1] + q3Frac * (dataSet[q3Floor] - dataSet[q3Floor - 1])

        IQR = q3Val - q1Val
        xMin = q1Val - 1.5 * IQR
        xMax = q3Val + 1.5 * IQR

        clean = [x for x in dataSet if xMin <= x <= xMax]
        return clean
  
    def groupData(self, dataSet):
        n = len(dataSet)
        numClasses = math.ceil(math.log(n)/math.log(2))
        minVal = dataSet[0]
        maxVal = dataSet[-1]
        classWidth = round((maxVal - minVal) / numClasses, 2)
        classHeight = classWidth + 0.01

        classes = {}
        start = minVal

        for i in range(1, numClasses + 1):
            end = start + classWidth
            key = f"C{i}"
            
            # Handling last to include max values
            if i == numClasses:
                freq = len([x for x in dataSet if start <= x <= end])
            else:
                freq = len([x for x in dataSet if start <= x < end])
            
            class_mark = round((start + end) / 2, 2)

            classes[key] = {
                "interval": f"{round(start, 2)} - {round(end, 2)}",
                "frequency": freq,
                "class_mark": class_mark,
                "angle": round((freq / n) * 360, 2)
            }

            start = end

        return classes

    def plotAllGraphs(self, groupedData):
        labels = []
        frequencies = []
        class_marks = []
        intervals = []

        for k, v in groupedData.items():
            labels.append(f"{k} (f={v['frequency']})")
            intervals.append(v["interval"])
            frequencies.append(v["frequency"])
            class_marks.append(v["class_mark"])


        #1. Pie Graph
        outside_labels = [f"{v['interval']} ({v['class_mark']})" for v in groupedData.values()]
        frequencies = [v["frequency"] for v in groupedData.values()]

        plt.figure(figsize=(6, 6))
        wedges, texts, autotexts = plt.pie(
            frequencies,
            labels=outside_labels,
            autopct=lambda pct: f"{int(round(pct * sum(frequencies) / 100.0))}",
            startangle=140,
            textprops={'color': "white"}
        )

        for text in texts:
            text.set_color('black')
            text.set_fontsize(8)

        for autotext in autotexts:
            autotext.set_fontsize(10)
            autotext.set_weight("bold")

        plt.title("Pie Chart: Frequency, Intervals, and Class Mark")
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

        # 2. Bar Graph
        plt.figure(figsize=(8, 5))
        plt.bar(intervals, frequencies, color='skyblue')
        plt.title("Bar Graph: Frequency Distribution")
        plt.xlabel("Class Intervals")
        plt.ylabel("Frequency")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # 3. Line Graph
        plt.figure(figsize=(8, 5))
        plt.plot(class_marks, frequencies, marker='o', color='green')
        plt.title("Line Graph: Class Marks vs Frequency")
        plt.xlabel("Class Mark")
        plt.ylabel("Frequency")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

        # 4. Area Graph – using frequency (NOT cumulative)
        plt.figure(figsize=(8, 5))
        plt.fill_between(class_marks, frequencies, color='lightblue', alpha=0.7)
        plt.plot(class_marks, frequencies, marker='o', color='blue')
        plt.title("Area Graph: Frequency vs Class Mark")
        plt.xlabel("Class Mark")
        plt.ylabel("Frequency")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

        # 5. Histogram
        plt.figure(figsize=(8, 5))
        plt.hist(class_marks, bins=len(class_marks), weights=frequencies, edgecolor='black', color='orchid')
        plt.title("Histogram: Frequency Distribution")
        plt.xlabel("Class Mark")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.show()
    
    def groupedMean(self, groupedData):
      total_fx = 0
      total_f = 0

      for v in groupedData.values():
          freq = v["frequency"]
          mark = v["class_mark"]
          total_fx += freq * mark
          total_f += freq

      mean = total_fx / total_f if total_f != 0 else 0
      return round(mean, 2)



if __name__ == "__main__":
    sol = Solution()
    input_data = [39.12, 61.74, 37.29, 44.35, 457.29, 64.1, 48.25, 67.25, 58.95,
                  39.95, 38.42, 55.8, 44.35, 38.75, 63.91, 1.5, 40.15, 60.29,
                  41.26, 49.32, 36.07, 46.01, 41.13, 67.29, 45.68, 63.55,
                  62.12, 36.85, 45.97, 42.89]
    result = sol.solution(input_data)
    for k, v in result.items():
      print(f"{k}: {v}")
    
    sol.plotAllGraphs(result)
    mean = sol.groupedMean(result)
    print("Grouped Mean:", mean)