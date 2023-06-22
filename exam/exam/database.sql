-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: std-mysql    Database: std_1760_exam
-- ------------------------------------------------------
-- Server version	5.7.26-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('b42e604f68a4');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `description` text,
  `year` year(4) NOT NULL,
  `publisher` varchar(30) NOT NULL,
  `author` varchar(30) NOT NULL,
  `rating_sum` int(11) NOT NULL,
  `rating_num` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_books_title` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (22,'Метро. Трилогия под одной обложкой','«Метро» Дмитрия Глуховского переведено на 37 языков мира и издано двухмиллионным тиражом.\n\nТретья мировая стерла человечество с лица Земли. Планета опустела. Мегаполисы обращены в прах и пепел. Железные дороги ржавеют. Спутники одиноко болтаются на орбите. Радио молчит на всех частотах. Выжили только те, кто услышав сирены тревоги, успел добежать до дверей московского метро. Там, на глубине в десятки метров, на станциях и в туннелях, люди пытаются переждать конец света. Там они создали новый мирок вместо потерянного огромного мира. Они цепляются за жизнь изо всех сил и отказываются сдаваться. Они мечтают однажды вернуться наверх – когда радиационный фон от ядерных бомбардировок спадет. И не оставляют надежды найти других выживших…\n\nПеред вами – наиболее полное коллекционное издание трилогии «Метро». Впервые «Метро 2033», «Метро 2034», «Метро 2035» и новелла «Евангелие от Артема» выходят под одной обложкой. Дмитрий Глуховский ставит точку в саге, над которой работал двадцать лет.\n\nНовелла «Евангелие от Артема» представлена эпилогом к роману «Метро 2033»',2015,' ЛитРес','Дмитрий Глуховский',0,0,1460),(23,'Дети времени','Доктор Аврана Керн проводит эксперимент по наделению животных разумом. Терраформированная планета должна стать домом для обезьян, с которыми спустя века Керн мечтает говорить как с равными. Но по Земле и ее колониям прокатывается война. Эксперимент и его наблюдатель отрезаны от всех.\n\nЧерез две тысячи лет на сигнал бедствия Керн прилетает корабль-ковчег с остатками человечества. Мир Керн его последняя надежда. Кажется, пропасть непонимания между последними людьми и экспериментальным видом непреодолима, ведь разум обрели не обезьяны, а совсем другой вид.',2019,' Эксмо','Адриан Чайковски',0,0,756),(24,'Брать, давать и наслаждаться.','Чувствовать себя полным сил. Вставать каждое утро с той ноги. Испытывать воодушевление, приступая к трудной задаче.\n\nНовая книга Татьяны Мужицкой – это уникальная система практик, которая поможет всегда оставаться в ресурсе. Даже когда из-за эпидемии нельзя рвануть на недельку в Тай или посидеть в ресторане с друзьями. Татьяна объясняет, как черпать жизненные силы из того, что не зависит от внешних обстоятельств. Ее подход основан на одноименном марафоне. Только в течение полугода его прошли более 1000 человек. Их отзывы говорят сами за себя: «\"Брать, давать и наслаждаться\" – это целая система отношений с собой и миром, превращающая нас в настоящий генератор вдохновения и бодрости».',2013,' Алтапресс','Татьяна Мужицкая',0,0,365),(25,'Случайный ребенок от миллиардера','Много лет назад я согласилась на авантюру, которая перевернула всю мою жизнь вверх дном. Из успешной модели я стала матерью одиночкой и бизнес-вумен. Теперь я растила сына одна и была вполне себе счастлива. Ровно до тех пор, пока не объявился незваный папа, заучивший на зубок все свои права.',2022,' Дрофа','Лия Рой',7,2,345),(32,'123','12e',2022,'123','123',0,0,500),(33,'Выбор. О свободе и внутренней силе человека','В шестнадцать лет Эдит Эгер мечтала о карьере балерины, но вместо театральной сцены девушку ждал… Аушвиц. Здесь она потеряла своих родителей, погибших в газовой камере. Вынуждена была танцевать перед нацистским офицером Йозефом Менгеле за буханку хлеба. Вместе с сестрой боролась за жизнь в лагерях смерти. Весной 1945 года Эдит оказалась в австрийском концлагере Гунскирхен. Здесь американские освободители и обнаружили истощенную и измученную девушку среди груды мертвых тел.\n\nОна сумела выжить. Создать семью, стать всемирно известным психологом. Но забыть и простить, равно как и научиться говорить об ужасах прошлого, она так и не смогла. Неужели единственный выход – томиться в тюрьме собственных страхов и чувства вины до конца жизни? Эдит предпочла выбрать иной вариант. Спустя тридцать пять лет она вернулась в Аушвиц, чтобы простить человека, которого обвиняла столько лет. Не Гитлера. Не Менгеле. Саму себя.\n\nСделав этот выбор, Эдит Эгер сумела исцелиться. С тех пор она помогала людям, страдающим от травматических стрессовых расстройств, найти свой путь к свободе от внутренних демонов. Результатом ее деятельности стала книга «Выбор». Вы можете читать ее онлайн или скачать в подходящем формате на ЛитРес.',2016,'Эксмо','Эдит Ева Эгер',0,0,500),(34,'Вторая жизнь Уве','На первый взгляд Уве – самый угрюмый человек на свете. Он, как и многие из нас, полагает, что его окружают преимущественно идиоты – соседи, которые неправильно паркуют свои машины; продавцы в магазине, говорящие на птичьем языке; бюрократы, портящие жизнь нормальным людям…\n\nНо у угрюмого ворчливого педанта – большое доброе сердце. И когда молодая семья новых соседей случайно повреждает его почтовый ящик, это становится началом невероятно трогательной истории об утраченной любви, неожиданной дружбе, бездомных котах и древнем искусстве сдавать назад на автомобиле с прицепом. Истории о том, как сильно жизнь одного человека может повлиять на жизни многих других.',2016,'Эксмо','Фредрик Бакман',0,0,500);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books_genres`
--

DROP TABLE IF EXISTS `books_genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books_genres` (
  `books_id` int(11) NOT NULL,
  `genres_id` int(11) NOT NULL,
  PRIMARY KEY (`books_id`,`genres_id`),
  KEY `fk_books_genres_genres_id_genres` (`genres_id`),
  CONSTRAINT `fk_books_genres_books_id_books` FOREIGN KEY (`books_id`) REFERENCES `books` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_books_genres_genres_id_genres` FOREIGN KEY (`genres_id`) REFERENCES `genres` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books_genres`
--

LOCK TABLES `books_genres` WRITE;
/*!40000 ALTER TABLE `books_genres` DISABLE KEYS */;
INSERT INTO `books_genres` VALUES (24,1),(25,1),(32,1),(33,1),(23,2),(25,2),(32,2),(34,2),(22,3),(25,3),(32,3),(23,4),(32,4);
/*!40000 ALTER TABLE `books_genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `covers`
--

DROP TABLE IF EXISTS `covers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `covers` (
  `id` varchar(100) NOT NULL,
  `file_name` varchar(100) NOT NULL,
  `mime_type` varchar(100) NOT NULL,
  `md5_hash` varchar(100) NOT NULL,
  `book_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_covers_md5_hash` (`md5_hash`),
  UNIQUE KEY `uq_covers_book_id` (`book_id`),
  CONSTRAINT `fk_covers_book_id_books` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `covers`
--

LOCK TABLES `covers` WRITE;
/*!40000 ALTER TABLE `covers` DISABLE KEYS */;
INSERT INTO `covers` VALUES ('01b948f5-ff16-499b-b5be-67915976234a','66181962-tatyana-muzhickaya-brat-davat-i-naslazhdatsya-kak-ostavatsya-v-resurse-cht.jpg','image/jpeg','efef081039e409af7b4960bc88b69e94',24),('32410b4b-d7f1-43b0-9254-954b1ab02b65','20690188-fredrik-bakman-vtoraya-zhizn-uve.jpg','image/jpeg','34fc748cd7d49205fd3c8c559baeb671',34),('52b79925-5eee-45bb-9ad1-4119f9aab562','48508375-edit-eva-eger-vybor.jpg','image/jpeg','a33d58e7ec81fef7fdbd43112f5de324',33),('8e9898e0-6c71-410e-8045-085d1fce53f6','22764358-dmitriy-gluhovskiy-metro-trilogiya-pod-odnoy-oblozhkoy.jpg','image/jpeg','9c204a10c178b67b5eeb6d4763383684',22),('a162ace7-0e64-4838-b7c7-ebb5a73abadc','67656398-liya-roy-32069877-sluchaynyy-rebenok-ot-milliardera.jpg','image/jpeg','f05af2dd84f0e28cd2b732c17f1601d8',25),('ea25a212-4a9a-4fab-ac22-0cd4bb59d3ad','51322780-adrian-chaykovski-deti-vremeni.jpg','image/jpeg','a6ab9ce224a0d4f1dd7586a97eb274bd',23);
/*!40000 ALTER TABLE `covers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genres`
--

DROP TABLE IF EXISTS `genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genres` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `genre_name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_genres_genre_name` (`genre_name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genres`
--

LOCK TABLES `genres` WRITE;
/*!40000 ALTER TABLE `genres` DISABLE KEYS */;
INSERT INTO `genres` VALUES (3,'Детектив'),(1,'Роман'),(4,'Ужасы'),(2,'Фантастика');
/*!40000 ALTER TABLE `genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviews` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `rating` int(11) NOT NULL,
  `text` text NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_reviews_user_id_users` (`user_id`),
  KEY `fk_reviews_book_id_books` (`book_id`),
  CONSTRAINT `fk_reviews_book_id_books` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_reviews_user_id_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES (1,NULL,3,5,'123','2022-06-22 20:17:42'),(2,25,1,5,'Интересная книга. Сюжет прямо таки заинтриговал. Читала на одном дыхании!!! Советую прочитать книгу любителям любовных романов и мелодрам.','2022-06-24 17:55:58'),(3,25,3,2,'Столько неграмотного текста..... ужас!','2022-06-24 17:56:32');
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_name` varchar(20) NOT NULL,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_roles_role_name` (`role_name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'admin','Суперпользователь, имеет полный доступ к системе, в том числе к созданию и удалению книг)'),(3,'moder','Может редактировать данные книг и производить модерацию рецензий'),(4,'user','Может оставлять рецензии');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `login` varchar(20) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `first_name` varchar(20) NOT NULL,
  `middle_name` varchar(20) DEFAULT NULL,
  `role_id` int(11) NOT NULL,
  `password_hash` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_users_login` (`login`),
  KEY `fk_users_role_id_roles` (`role_id`),
  CONSTRAINT `fk_users_role_id_roles` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin','Иван','Иванов',NULL,1,'pbkdf2:sha256:260000$h7qlIrYV4TPaM882$525042ace32ebb16fce6ef4bec96b7db4aef4ce639db3ccaa17a839795db45da'),(2,'moder','Иван','Иванов',NULL,3,'pbkdf2:sha256:260000$dRjOaBYRJTLCvQo2$b68ce5d72b61e4b88672c78f49fd5a4d9400a43ef51c8b54ef6a0debfdb64749'),(3,'user','Иван','Иванов',NULL,4,'pbkdf2:sha256:260000$2z4JAfjm9J4axs6T$407088077f78fdc6ac608470f6dee2babda0b12cd4c98af2fa667a290edb3ffb');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-28 11:00:57
