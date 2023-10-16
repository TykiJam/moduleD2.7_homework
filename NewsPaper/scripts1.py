#python -m venv venv
#venv\Scripts\activate.bat
#cd NewsPaper 
#python manage.py makemigrations
#python manage.py migrate 
#python manage.py shell
#exec(open('scripts1.py').read())
#from news.models import *

from news.models import *

#Создаем пользоватлей и авторов
user1 = User.objects.create(username='User12', first_name='Test1')
Author.objects.create(authorUser=user1)
user2 = User.objects.create(username='User21', first_name='Test2')
Author.objects.create(authorUser=user2)


#Создаем категории
Category.objects.create(name='IT')
Category.objects.create(name='Science')
Category.objects.create(name='Politics')
Category.objects.create(name='Weather')


#Создаем статьи и новости
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='User12')), categoryType='NW', title='News1', text='This is a news.')
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='User12')), categoryType='AR', title='Article1', text='This is an article.')
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='User21')), categoryType='NW', title='News2', text='This is different news.')
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='User21')), categoryType='AR', title='Article2', text='This is another article.')


#Получаем обьекты статей
p1 = Post.objects.get(pk=1)
p2 = Post.objects.get(pk=2)
p3 = Post.objects.get(pk=3)
p4 = Post.objects.get(pk=4)


#Получаеи обьекты категорий
c1 = Category.objects.get(name='IT')
c2 = Category.objects.get(name='Science')
c3 = Category.objects.get(name='Politics')
c4 = Category.objects.get(name='Weather')


#Добавляем категории к статьям
p1.postCategory.add(c1, c3)
p2.postCategory.add(c1, c2, c3, c4)
p3.postCategory.add(c3, c2)
p4.postCategory.add(c4, c1)


#Создаем комментарии
Comment.objects.create(commentUser=User.objects.get(username='User12'), commentPost = Post.objects.get(pk=1), text='1edw3et456')
Comment.objects.create(commentUser=User.objects.get(username='User21'), commentPost = Post.objects.get(pk=1), text='123rf24y')
Comment.objects.create(commentUser=User.objects.get(username='User12'), commentPost = Post.objects.get(pk=2), text='12r35')
Comment.objects.create(commentUser=User.objects.get(username='User21'), commentPost = Post.objects.get(pk=3), text='12346')
Comment.objects.create(commentUser=User.objects.get(username='User21'), commentPost = Post.objects.get(pk=4), text='12342567')


#Рейтинги обьктов
Post.objects.get(pk=1).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=1).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=2).like()
Post.objects.get(pk=3).like()
Post.objects.get(pk=3).like()
Post.objects.get(pk=4).dislike()
Post.objects.get(pk=2).dislike()
Post.objects.get(pk=1).dislike()
Comment.objects.get(pk=1).like()
Comment.objects.get(pk=1).like()
Comment.objects.get(pk=1).dislike()
Comment.objects.get(pk=2).like()
Comment.objects.get(pk=2).like()
Comment.objects.get(pk=2).like()
Comment.objects.get(pk=2).dislike()
Comment.objects.get(pk=3).like()


#Обновляем рейтинг авторов
Author.objects.get(authorUser = User.objects.get(username="User12")).update_rating()
Author.objects.get(authorUser = User.objects.get(username="User21")).update_rating()
a = Author.objects.get(authorUser = User.objects.get(username="User12"))
b = Author.objects.get(authorUser = User.objects.get(username="User21"))
a.ratingAuthor
b.ratingAuthor


#Выводим информацию о лучшем авторе
#Author.objects.get(authorUser = User.objects.get(username="User12")).ratingAuthor
#bestUser = Author.objects.all().order_by('-ratingAuthor').values('authorUser', 'ratingAuthor') [0]
#print(bestUser)
bestAuthor = Author.objects.order_by('-ratingAuthor').first()
print(f'Имя пользователя: {bestAuthor.authorUser.username}, Рейтинг: {bestAuthor.ratingAuthor}')

#Вывести дату добавления, 
# username автора, рейтинг, заголовок и превью 
# лучшей статьи, # основываясь на лайках/дислайках к этой статье.

bestPost=Post.objects.order_by("-rating")[:1].values("dateCreation","author__authorUser__username","rating","title","text")
print(bestPost)


#Вывести все комментарии
#(дата, пользователь, рейтинг, текст) к этой статье.

commments=Comment.objects.order_by("-rating")[:1].values("dateCreation","commentUser__username","rating","text")
print(commments)
