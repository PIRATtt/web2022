-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Хост: std-mysql
-- Время создания: Ноя 09 2022 г., 22:25
-- Версия сервера: 5.7.26-0ubuntu0.16.04.1
-- Версия PHP: 8.0.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `std_1929_exam`
--

-- --------------------------------------------------------

--
-- Структура таблицы `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('4d4c5c5c25f5');

-- --------------------------------------------------------

--
-- Структура таблицы `books`
--

CREATE TABLE `books` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `short_description` text NOT NULL,
  `year` int(11) NOT NULL,
  `publishing_house` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `pages` int(11) NOT NULL,
  `rating_sum` int(11) NOT NULL,
  `rating_num` int(11) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `books`
--

INSERT INTO `books` (`id`, `name`, `short_description`, `year`, `publishing_house`, `author`, `pages`, `rating_sum`, `rating_num`, `created_at`) VALUES
(18, 'Мартин Иден', 'Мартин Иден – рабочий парень, моряк, выходец из низов случайно знакомится с Руфью Морз – девушкой из состоятельной буржуазной семьи. Желая стать достойным нее и попав под обаяние высшего общества Мартин берется за самообразование. Узнав, что журналы платят приличные гонорары авторам рассказов Мартин берется за писательство будучи уверенным, что может писать гораздо лучше других.', 1909, 'Москва', 'Джек Лондон', 1500, 0, 0, '2022-11-08 20:50:02'),
(19, 'Над пропастью во ржи', 'Роман «Над пропастью во ржи» – это история о том, как Холден пытается наладить отношения с другими людьми и терпит неудачу, что заставляет его бояться зрелости и цепляться за идеализированное представление о детстве. Большая часть книги рассказывает о поисках Холденом связи, следуя за ним через десятки больших и малых встреч с таксистами, монахинями, туристами, сутенёрами, бывшими одноклассниками и многими другими.', 1951, 'Москва', 'Дж. Д. Сэлинджер', 215, 0, 0, '2022-11-08 21:03:11'),
(20, 'Преступление и наказание', 'Наказание есть мера государственного принуждения, назначаемая по приговору суда. Наказание применяется к лицу, признанному виновным в совершении преступления, и заключается в предусмотренных УК РФ лишении или ограничении прав и свобод этого лица. Наказание применяется в целях восстановления социальной справедливости, а также в целях исправления осужденного и предупреждения совершения новых преступлений.', 1866, 'Санкт-Петербург', 'Ф. М. Достоевский', 600, 5, 2, '2022-11-08 21:50:32'),
(21, 'Призрак в Сети. Мемуары величайшего хакера', 'Кевин Митник по праву считается самым неуловимым мастером компьютерного взлома в истории. Он проникал в сети и компьютеры крупнейших мировых компаний, и как бы оперативно ни спохватывались власти, Митник был быстрее, вихрем проносясь через телефонные коммутаторы, компьютерные системы и сотовые сети. Он долгие годы рыскал по киберпространству, всегда опережая преследователей не на шаг, а на три шага, и заслужил славу человека, которого невозможно остановить. Но для Митника хакерство не сводилось только к технологическим эпизодам, он плел хитроумные сети обмана, проявляя редкое коварство и выпытывая у ничего не подозревающего собеседника ценную информацию.\n\n«Призрак в Сети» – захватывающая невыдуманная история интриг, саспенса и невероятных побегов. Это портрет провидца, обладающего такой изобретательностью, хваткой и настойчивостью, что властям пришлось полностью переосмыслить стратегию погони за ним. Отголоски этой эпической схватки чувствуются в сфере компьютерной безопасности и сегодня.', 2012, 'Эксмо', 'Кевин Митник', 610, 0, 0, '2022-11-09 17:12:09'),
(22, 'Финансист', 'Американский романист Теодор Драйзер давно занял почетное место среди классиков мировой литературы. Тема большого бизнеса, людей, как преуспевших в нем, так и потерпевших фиаско, привлекала внимание Т. Драйзера еще в те годы, когда он занимался журналистикой.\n\nГерой романа «Финансист» – Фрэнк Каупервуд – не только удачливый бизнесмен и владелец огромного состояния. Он обладает особым магнетизмом, сверхъестественной властью как над мужчинами, так и над женщинами. Богатство для него не цель, а средство, позволяющее Каупервуду жить, руководствуясь принципом: «Мои желания прежде всего».', 1912, 'Эксмо', 'Теодор Драйзер', 610, 0, 0, '2022-11-09 17:15:21');

-- --------------------------------------------------------

--
-- Структура таблицы `book_genres`
--

CREATE TABLE `book_genres` (
  `id` int(11) NOT NULL,
  `book_id` int(11) NOT NULL,
  `genre_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `book_genres`
--

INSERT INTO `book_genres` (`id`, `book_id`, `genre_id`) VALUES
(15, 19, 1),
(16, 20, 4),
(19, 21, 4),
(18, 18, 5),
(20, 22, 5);

-- --------------------------------------------------------

--
-- Структура таблицы `covers`
--

CREATE TABLE `covers` (
  `id` varchar(100) NOT NULL,
  `file_name` varchar(100) NOT NULL,
  `mime_type` varchar(100) NOT NULL,
  `md5_hash` varchar(100) NOT NULL,
  `book_id` int(11) DEFAULT NULL,
  `object_id` int(11) DEFAULT NULL,
  `object_type` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `covers`
--

INSERT INTO `covers` (`id`, `file_name`, `mime_type`, `md5_hash`, `book_id`, `object_id`, `object_type`) VALUES
('165428e8-5ca4-4200-9f73-64c5c3670cca', '4436342-vilyam-saymon-prizrak-v-seti-memuary-velichayshego-hakera.jpg', 'image/jpeg', 'c2b25a087f6c22e78af05daa7c9797ac', 21, NULL, 'books'),
('6d0a379d-4089-4a03-ad67-fc5b9eb95cfc', '274px-The_Catcher_in_the_Rye_1951_first_edition_cover.jpg', 'image/jpeg', '4466a9369010e5f192013dbfb22254d4', 19, NULL, 'books'),
('8ca8e131-307e-4db3-83f5-faf39790ba15', '6138765857.jpg', 'image/jpeg', '00e11db33099ba4e0131ddacb9414fd9', 20, NULL, 'books'),
('fca45550-fb0f-4f22-a153-5c6e6d9342d7', 'Martin_Eden.jpg', 'image/jpeg', '3f5804cf35aebc7052bcaa2d4001eb60', 18, NULL, 'books'),
('feedce5f-e8de-4f13-b918-a748767e7379', '80581.750x0.jpg', 'image/jpeg', '7ebc479b053832881b12311ba9cf53c5', 22, NULL, 'books');

-- --------------------------------------------------------

--
-- Структура таблицы `genres`
--

CREATE TABLE `genres` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `genres`
--

INSERT INTO `genres` (`id`, `name`) VALUES
(4, 'Детектив'),
(1, 'Классика'),
(3, 'Комедия'),
(5, 'Роман'),
(2, 'Фантастика');

-- --------------------------------------------------------

--
-- Структура таблицы `reviews`
--

CREATE TABLE `reviews` (
  `id` int(11) NOT NULL,
  `book_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `rating` int(11) NOT NULL,
  `text` text NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `reviews`
--

INSERT INTO `reviews` (`id`, `book_id`, `user_id`, `rating`, `text`, `created_at`) VALUES
(12, 20, 2, 5, '10/10', '2022-11-08 22:02:06'),
(13, 20, 3, 0, '0/10', '2022-11-08 22:03:22');

-- --------------------------------------------------------

--
-- Структура таблицы `roles`
--

CREATE TABLE `roles` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `roles`
--

INSERT INTO `roles` (`id`, `name`, `description`) VALUES
(1, 'admin', 'chelick'),
(2, 'moder', 'can do some stuff'),
(3, 'user', 'can see photos');

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `login` varchar(100) NOT NULL,
  `password_hash` varchar(200) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `middle_name` varchar(100) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`id`, `login`, `password_hash`, `last_name`, `first_name`, `middle_name`, `role_id`) VALUES
(1, 'user', 'pbkdf2:sha256:260000$lwGPhjCwaMIfREVn$2fd3f2b12b1d51a03a8ff88e52966760ad125ea7bcdcb958a4c5300c251b53b1', 'Admin', 'Admin', '', 1),
(2, 'user2', 'pbkdf2:sha256:260000$JFvPvy1YsFFvOGWM$e45d1dffbe4f2b6dfc0b5917399c344e497cee3f3a73a5921931f68fa0844e2f', 'Moder', 'Moder', '', 2),
(3, 'user3', 'pbkdf2:sha256:260000$JFvPvy1YsFFvOGWM$e45d1dffbe4f2b6dfc0b5917399c344e497cee3f3a73a5921931f68fa0844e2f', 'User', 'User', 'User', 3);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Индексы таблицы `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `book_genres`
--
ALTER TABLE `book_genres`
  ADD PRIMARY KEY (`id`,`book_id`,`genre_id`),
  ADD KEY `fk_book_genres_genre_id_genres` (`genre_id`),
  ADD KEY `fk_book_genres_book_id_books` (`book_id`);

--
-- Индексы таблицы `covers`
--
ALTER TABLE `covers`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uq_covers_md5_hash` (`md5_hash`),
  ADD KEY `fk_covers_book_id_books` (`book_id`);

--
-- Индексы таблицы `genres`
--
ALTER TABLE `genres`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uq_genres_name` (`name`);

--
-- Индексы таблицы `reviews`
--
ALTER TABLE `reviews`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_reviews_user_id_users` (`user_id`),
  ADD KEY `fk_reviews_book_id_books` (`book_id`);

--
-- Индексы таблицы `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uq_users_login` (`login`),
  ADD KEY `fk_users_role_id_roles` (`role_id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `books`
--
ALTER TABLE `books`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT для таблицы `book_genres`
--
ALTER TABLE `book_genres`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT для таблицы `genres`
--
ALTER TABLE `genres`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `reviews`
--
ALTER TABLE `reviews`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT для таблицы `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `book_genres`
--
ALTER TABLE `book_genres`
  ADD CONSTRAINT `fk_book_genres_book_id_books` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `fk_book_genres_genre_id_genres` FOREIGN KEY (`genre_id`) REFERENCES `genres` (`id`);

--
-- Ограничения внешнего ключа таблицы `covers`
--
ALTER TABLE `covers`
  ADD CONSTRAINT `fk_covers_book_id_books` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`) ON DELETE CASCADE;

--
-- Ограничения внешнего ключа таблицы `reviews`
--
ALTER TABLE `reviews`
  ADD CONSTRAINT `fk_reviews_book_id_books` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `fk_reviews_user_id_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Ограничения внешнего ключа таблицы `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `fk_users_role_id_roles` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
