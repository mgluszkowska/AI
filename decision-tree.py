		# kod znajdujacy sie w metodzie __init__ 
		
		# zbieranie danych do uczenia maszynowego
		
		self.collectData()
		
		# wczytanie danych z pliku i przygotowanie ich do uczenia maszynowego

		col_names = ['waiterX', 'waiterY', 'whatKeep', 'table1', 'table2', 'table3', 'table4', 'lada1', 'lada2',
                     'lada3', 'dest']
        df = pd.read_csv("./file.csv", header=None, names=col_names)
        x = df.drop(["dest"], axis=1)
        y = df["dest"]
		
		# podzial danych na dane do nauki i dane testowe

        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

		# stworzenie drzewa decyzyjnego
		
        classifier = DecisionTreeClassifier(criterion="entropy")
        classifier.fit(X_train, y_train)
        y_pred = classifier.predict(X_test)
        print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
		
		# wykorzystanie drzewa do proby rozwiazania planszy bez udzialu czlowieka

        self.play(classifier)
		
		******************************************************************************
		#metoda odpowiedzialna za zbieranie danych do uczenia maszynowego
		def collectData(self):
        csvFile = open("./file.csv", "a")
        writer = csv.writer(csvFile)
        while True:
            row = [self.waiter.positionX, self.waiter.positionY,
                    self.waiter.whatKeep,
                    self.tableList[0].showStan(), self.tableList[1].showStan(), self.tableList[2].showStan(),
                    self.tableList[3].showStan(),
                    self.orderTableList[0].stanLady(), self.orderTableList[1].stanLady(),
                    self.orderTableList[2].stanLady()]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
					
            #czekanie na numerki z klawiatury i odnajdywanie bfs do danego obiektu
            keys = pygame.key.get_pressed()
            if keys[pygame.K_0]:
                self.bfs(self.waiter, 0, [])
                row.append(0)
                writer.writerow(row)
            if keys[pygame.K_1]:
                self.bfs(self.waiter, 1, [])
                row.append(1)
                writer.writerow(row)
            if keys[pygame.K_2]:
                self.bfs(self.waiter, 2, [])
                row.append(2)
                writer.writerow(row)
            if keys[pygame.K_3]:
                self.bfs(self.waiter, 3, [])
                row.append(3)
                writer.writerow(row)
            if keys[pygame.K_4]:
                self.bfs(self.waiter, 4, [])
                row.append(4)
                writer.writerow(row)
            if keys[pygame.K_5]:
                self.bfs(self.waiter, 5, [])
                row.append(5)
                writer.writerow(row)
            if keys[pygame.K_6]:
                self.bfs(self.waiter, 6, [])
                row.append(6)
                writer.writerow(row)
            if keys[pygame.K_7]:
                self.bfs(self.waiter, 7, [])
                row.append(7)
                writer.writerow(row)
            if keys[pygame.K_9]:
                break;

            self.draw()
            self.waiter.move(self)
            self.fpsClock.tick(10)

        csvFile.close()
		
	# metoda odpowiedzialna za probe rozwiazania planszy za pomoca sztucznej inteligencji
	 def play(self, classifier):
        success = 0
        while success < 7:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
					
			# zebranie aktualnych danych o planszy			
            row = [[self.waiter.positionX, self.waiter.positionY,
                    self.waiter.whatKeep,
                    self.tableList[0].showStan(), self.tableList[1].showStan(), self.tableList[2].showStan(),
                    self.tableList[3].showStan(),
                    self.orderTableList[0].stanLady(), self.orderTableList[1].stanLady(),
                    self.orderTableList[2].stanLady()]]
			
			# drzewo przewiduje nastepny ruch na podstawie danych
            prediction = classifier.predict(row)
            result = prediction.tolist()
            print(result[0])
			
			# kelner udaje sie do odpowiedniej pozycji na planszy wyznaczonej przez drzewo
            self.bfs(self.waiter, result[0], [])
            success += 1
            self.draw()
            self.waiter.move(self)
            self.fpsClock.tick(10)