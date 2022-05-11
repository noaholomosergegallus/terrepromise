from articles.models import Articles
def run():
    for i in range(5,15):
        article=Articles()
        article.title='Article N* #%d'%i
        article.content='contenu Article N* #%d'%i
        article.image="http://default"
        article.save()
        print('operation reussi')