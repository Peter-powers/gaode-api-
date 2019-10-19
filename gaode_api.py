#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pprint


# In[2]:


key='yourkey'


# In[12]:


def geocode():
    url = 'https://restapi.amap.com/v3/geocode/geo?parameters'
    data = {
        'key':key,
        'address':'北京市朝阳区阜通东大街6号'
    }
    r=requests.get(url,data)
    return r.json()


# In[13]:


geocode()


# In[14]:


def direction():
    url = 'https://restapi.amap.com/v3/direction/walking?parameters'
    data = {
        'key':key,
        'origin':'116.481028,39.989643',
        'destination':'116.434446,39.90816'
       
    }
    r=requests.get(url,data)
    return r.json()


# In[15]:


direction()


# In[25]:


def district(i):
    url = 'https://restapi.amap.com/v3/config/district?parameters'
    data = {
        'key':key,
        'keyword':i,
       'subdistrict':3
    }
    r=requests.get(url,data)
    return r.json()


# In[26]:


district('广东')


# In[28]:


def place(i):
    url = 'https://restapi.amap.com/v3/place/text?parameters'
    data = {
        'key':key,
        'keywords':i, #输入相关关键词
        'city':'广州'
       
    }
    r=requests.get(url,data)
    return r.json()


# In[29]:


place('电影院')


# In[30]:


def ip():
    url = 'https://restapi.amap.com/v3/ip?parameters'
    data = {
        'key':key
      
       
    }
    r=requests.get(url,data)
    return r.json()


# In[31]:


ip()


# In[ ]:


def direction():
    url = 'https://restapi.amap.com/v3/direction/walking?parameters'
    data = {
        'key':key,
        'origin':'116.481028,39.989643',
        'destination':'116.434446,39.90816'
       
    }
    r=requests.get(url,data)
    return r.json()


# In[119]:


from skimage import io


# In[126]:


def staticmap():
    url = 'https://restapi.amap.com/v3/staticmap?parameters'
    data = {
        'key':key,
        'location':"116.481485,39.990464",
        'zoom':"10",
        'size':"750*300",    
       
    }
    r=requests.get(url,data)
    return r


# In[127]:


d=staticmap()


# In[129]:


d.headers


# In[138]:


from PIL import Image
from io import BytesIO


# In[139]:


image = Image.open(BytesIO(d.content))
image.save('map.png')


# In[141]:


from IPython.display import Image
from IPython.core.display import HTML 
Image(filename ='map.png')


# In[41]:


def coordinate():
    url = 'https://restapi.amap.com/v3/assistant/coordinate/convert?parameters'
    data = {
        'key':key,
        'locations':'116.481028,39.989643,116.434446,39.90816',
       
       
    }
    r=requests.get(url,data)
    return r.json()


# In[43]:


coordinate()


# In[45]:


def weather():
    url = 'https://restapi.amap.com/v3/weather/weatherInfo?parameters'
    data = {
        'key':key,
        'city':'110000',
      
    }
    r=requests.get(url,data)
    return r.json()


# In[46]:


weather()


# In[54]:


def inputtips(i):
    url = 'https://restapi.amap.com/v3/assistant/inputtips?parameters'
    data = {
        'key':key,
        'keywords':i,
       'type':'050301',
        'location':'116.481488,39.990464',
        'city':'广州',
       'datatype':'all'
    }
    r=requests.get(url,data)
    return r.json()


# In[55]:


inputtips('广州')


# In[61]:


def traffic():
    url = 'https://restapi.amap.com/v3/traffic/status/rectangle?parameters'
    data = {
        'key':key,
        'rectangle':'116.351147,39.966309;116.357134,39.968727'
       
    }
    r=requests.get(url,data)
    return r.json()


# In[62]:


traffic()


# In[89]:


def geofence_meta(i):
    url = 'https://restapi.amap.com/v4/geofence/meta?key='+key
    
    data ={
         'name':i,
        'center':'115.672126,38.817129',
        'radius':'5000',
        'repeat': "Mon,Tues,Wed,Thur,Fri,Sat,Sun"
    }
    r=requests.post(url,json=data)
    return r.json()


# In[90]:


geofence_meta('可要开心')


# In[94]:


def grasproad_driving():
    url = 'https://restapi.amap.com/v4/grasproad/driving?key='+key
    data = {
"x": 116.449429,
"y": 40.014844,
"sp": 4,
"ag": 110,
"tm": 1478831753
}, {
"x": 116.449639,
"y": 40.014776,
"sp": 3,
"ag": 110,
"tm": 23
}, {
"x": 116.449859,
"y": 40.014716,
"sp": 3,
"ag": 111,
"tm": 33
}, {
"x": 116.450074,
"y": 40.014658,
"sp": 3,
"ag": 110,
"tm": 31
}, {
"x": 116.450273,
"y": 40.014598,
"sp": 3,
"ag": 111,
"tm": 20
}
    r=requests.post(url,json=data)
    return r.json()


# In[95]:


grasproad_driving()


# ## 智能指路
# ### 场景：用户突然想去电影院看电影
# ### 使用流程：1、用户通过手机输入电影院 2、应用反馈附近的电影院信息 3、用户选择其中任一 4、应用进行指路 5、到达目的地提醒
# ### 使用功能：1、地理编码api（获取用户地理位置信息）2、poi查询（通过用户地理位置信息，从而获得附近电影院地理位置信息）3、轨迹纠偏（通过实时的获取用户地理位置，从而对其向目的地的指引做出调整）4、静态地图（仅作为用户大致了解位置提供帮助）
# 
