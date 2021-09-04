from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from blog import models 
import graphene

class TipoUsuario(DjangoObjectType):
    class Meta:
        model = get_user_model


class TipoAutor(DjangoObjectType):
    class Meta:
        model = models.Perfil

class PostType(DjangoObjectType):
    class Meta:
        model = models.Tag



class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)
    autor_by_username = graphene.Field(TipoAutor, username=graphene.String())
    post_by_slug = graphene.Field(PostType, slug=graphene.String())
    post_by_author = graphene.List(PostType, username = graphene.String())
    post_by_tag = graphene.List(PostType, tag=graphene.String())

    def resolve_all_post(root, info):
        return(
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .all()
        )

    def resolve_author_by_username(root,info, username):
        return(
            models.Perfil.objects.select_related("user").get(
                user__unsername = username
            )
        )

    
    def resolve_post_by_slug(root, info, slug):
        return(
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .get(slug=slug)
        )

    def resolve_post_by_author(root, info, username):
        return(
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .filter(author__user__username=username)
        )
    
    def resolve_post_by_tag(root, info, tag):
        return(
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .filter(tags__name__iexact=tag)
        )

schema = graphene.Schema(query=Query)