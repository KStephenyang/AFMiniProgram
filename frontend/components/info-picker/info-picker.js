// components/info-picker/info-picker.js
Component({
  /**
   * 组件的属性列表
   */
  properties: {
    item: {
      type: String
    },
    array: {
      type: Array
    }
  },

  /**
   * 组件的初始数据
   */
  data: {
    item_value: '',
    index: 0
  },

  /**
   * 组件的方法列表
   */
  methods: {
    bindPickerChange: function (e) {
      console.log('picker发送选择改变，携带值为', e.detail.value)
      this.setData({
        index: e.detail.value
      })
    },
  }
})
