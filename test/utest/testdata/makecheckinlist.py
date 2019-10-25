from emyxin.models import checkinlist
from emyxin.serializers import CheckinlistSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

checkinlist = checkinlist(title='奥尔夫音乐课',singner='李越')
checkinlist.save()

if __name__ == '__main__':
    main()