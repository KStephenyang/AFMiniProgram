// components/activity-publish/publish.js
Component({
  /**
   * 组件的属性列表
   */
  properties: {
    meeting_time: {
      type: String
    },
    meeting_location: {
      type: String
    },
    meeting_topic: {
      type: String
    },
    guest: {
      type: String
    },
    meeting_type: {
      type: String
    },
    club: {
      type: String
    }
  },

  /**
   * 组件的初始数据
   */
  data: {
    club_array: ['AmazingFriday', 'LightHouse', 'ZTalk'],
    meeting_type_array: ['Week Meeting', 'Month Meeting'],
    meeting_time_array: ['2019-2-1 19:00', '2019-2-8 19:00', '2019-2-15 19:00']
  },

  /**
   * 组件的方法列表
   */
  methods: {

  }
})
