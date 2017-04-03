from api.serializers import ContestSerializer
from contests.models import Contest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def contest_list(request):
    """
    List all contests.
    """
    contests = Contest.objects.all()
    serializer = ContestSerializer(contests, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def contest_detail(request, pk):
    """
    Get, udpate, or delete a specific contest
    """
    try:
        contest = Contest.objects.get(pk=pk)
    except Contest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ContestSerializer(contest)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContestSerializer(contest, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        contest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)