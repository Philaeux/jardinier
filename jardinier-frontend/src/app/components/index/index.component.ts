import { Component, HostListener, OnInit } from '@angular/core'
import { ApiService } from '../../services/api.service'
import { NgxChartsModule } from "@swimlane/ngx-charts"

@Component({
  selector: 'app-index',
  imports: [
    NgxChartsModule
  ],
  templateUrl: './index.component.html',
  styleUrl: './index.component.scss'
})
export class IndexComponent implements OnInit {

  constructor(private apiService: ApiService) { }

  callBackend: string = "Not processed"

  ngOnInit(): void {

    /** Example of call to the backend */
    this.apiService.querySuccessExample().subscribe((response) => {
      if (response.data.querySuccessExample.__typename == "ApiSuccess") {
        this.callBackend = "Success !"
      }
    })

  }

  view: [number, number] = [window.innerWidth * 0.95, window.innerHeight / 2 * 0.95];

  @HostListener('window:resize', ['$event'])
  onResize() {
    this.view = [window.innerWidth * 0.95, window.innerHeight / 2 * 0.95]
  }

  mockDataTemp = [
    {
      "name": "Température",
      "series": [
        {
          "value": 20,
          "name": "2016-09-19T21:17:52.618Z"
        },
        {
          "value": 25,
          "name": "2016-09-14T09:12:52.243Z"
        },
        {
          "value": 30,
          "name": "2016-09-24T03:36:21.195Z"
        },
        {
          "value": 28,
          "name": "2016-09-19T23:01:26.514Z"
        },
        {
          "value": 22,
          "name": "2016-09-19T14:48:19.814Z"
        }
      ]
    },
  ]

  mockDataHum = [
    {
      "name": "Humidité",
      "series": [
        {
          "value": 20,
          "name": "2016-09-19T21:17:52.618Z"
        },
        {
          "value": 25,
          "name": "2016-09-14T09:12:52.243Z"
        },
        {
          "value": 30,
          "name": "2016-09-24T03:36:21.195Z"
        },
        {
          "value": 28,
          "name": "2016-09-19T23:01:26.514Z"
        },
        {
          "value": 22,
          "name": "2016-09-19T14:48:19.814Z"
        }
      ]
    },
  ]
}
