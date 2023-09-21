from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from products.models import Access, Lesson, LessonView, Product, User


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def user_lessons(request):
    """Уроки пользователя."""
    user = request.user
    lessons = Lesson.objects.filter(products__access__user=user).distinct()
    serialized_lessons = []
    for lesson in lessons:
        try:
            lesson_view = LessonView.objects.get(user=user, lesson=lesson)
            serialized_lessons.append(
                {
                    "lesson_id": lesson.id,
                    "title": lesson.title,
                    "video_url": lesson.video_url,
                    "duration_seconds": lesson.duration_seconds,
                    "status": lesson_view.status,
                    "viewed_time_seconds": lesson_view.viewed_time_seconds,
                }
            )
        except LessonView.DoesNotExist:
            serialized_lessons.append(
                {
                    "lesson_id": lesson.id,
                    "title": lesson.title,
                    "video_url": lesson.video_url,
                    "duration_seconds": lesson.duration_seconds,
                    "status": "Не просмотрено",
                    "viewed_time_seconds": 0,
                }
            )

    return Response(serialized_lessons)


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def product_lessons(request, product_id):
    """Просмотр продуктов по id"""
    user = request.user
    try:
        product = Product.objects.get(id=product_id, access__user=user)
    except Product.DoesNotExist:
        return Response(
            {"error": "У вас нет доступа к этому продукту"}, status=403
        )

    lessons = Lesson.objects.filter(products=product)

    serialized_lessons = []
    for lesson in lessons:
        try:
            lesson_view = LessonView.objects.get(user=user, lesson=lesson)
            serialized_lessons.append(
                {
                    "lesson_id": lesson.id,
                    "title": lesson.title,
                    "video_url": lesson.video_url,
                    "duration_seconds": lesson.duration_seconds,
                    "status": lesson_view.status,
                    "viewed_time_seconds": lesson_view.viewed_time_seconds,
                }
            )
        except LessonView.DoesNotExist:
            serialized_lessons.append(
                {
                    "lesson_id": lesson.id,
                    "title": lesson.title,
                    "video_url": lesson.video_url,
                    "duration_seconds": lesson.duration_seconds,
                    "status": "Не просмотрено",
                    "viewed_time_seconds": 0,
                }
            )

    return Response(serialized_lessons)


@api_view(["GET"])
@permission_classes([permissions.IsAdminUser])
def product_stats(request):
    """Статистика по продуктам. Только для админа."""
    user = request.user
    products = Product.objects.all()

    serialized_products = []
    for product in products:
        viewed_lessons = LessonView.objects.filter(
            user=user, lesson__products=product, status="Просмотрено"
        )
        total_viewed_lessons = viewed_lessons.count()
        total_viewed_time = sum(
            lesson_view.viewed_time_seconds for lesson_view in viewed_lessons
        )
        total_students = Access.objects.filter(product=product).count()
        product_purchase_percentage = (
            total_students / User.objects.count()
        ) * 100

        serialized_products.append(
            {
                "product_id": product.id,
                "product_name": product.name,
                "total_viewed_lessons": total_viewed_lessons,
                "total_viewed_time_seconds": total_viewed_time,
                "total_students": total_students,
                "product_purchase_percentage": product_purchase_percentage,
            }
        )

    return Response(serialized_products)
