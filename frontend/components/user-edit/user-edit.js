// components/user-edit/user-edit.js
Component({
  /**
   * 组件的属性列表
   */
  properties: {
    my_name: {
      type: String
    },
    my_club: {
      type: String
    },
    my_level: {
      type: String
    },
    my_role: {
      type: String
    },
    my_duty: {
      type: String
    },
    my_mentor: {
      type: String
    }
  },

  /**
   * 组件的初始数据
   */
  data: {
    club_array: ['AmazingFriday', 'LightHouse', 'ZTalk'],
    level_array: ['FreshMan', 'Pathway'],
    role_array: ['Officer', 'PR', 'President'],
    duty_array: ['Ah conter', 'LightHouse', 'ZTalk'],
    mentor_array: ['Kelly', 'Leaf', 'May']
  },

  /**
   * 组件的方法列表
   */
  methods: {

  }
})
