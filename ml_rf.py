from sklearn import tree
X = [[182,3234,3443],[34,343,454],[34,565,676],[234,454,676],[435,676,78],[123,234,676],[67,345,23],[34,465,678],[234,234,454],[234,34,45]]
Y = ['jantan','betina','jantan','jantan','jantan','betina','betina','betina','jantan','betina']
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)
prediction = clf.predict([[1,23,3]])
print prediction 
