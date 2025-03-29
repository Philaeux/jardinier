import { Component, HostListener, OnInit } from '@angular/core'
import { NgxChartsModule } from "@swimlane/ngx-charts"
import { Chart } from '../../models'
import { ApiService } from '../../services/api.service'


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

  view: [number, number] = [window.innerWidth * 0.95, window.innerHeight / 2 * 0.95];
  dataTemp: Chart[] = [
    {
      name: "Température",
      series: []
    },
  ]
  dataHum: Chart[] = [
    {
      "name": "Humidité",
      "series": []
    },
  ]
  offset: number = 0
  limit: number = 1000


  ngOnInit(): void {
    this.refreshData()
  }

  refreshData() {
    this.apiService.measures(this.limit, this.offset).subscribe((response) => {
      this.dataTemp = [
        {
          name: "Température",
          series: response.data.measures.map(measure => {
            return {
              name: new Date(measure.time),
              value: measure.temperature
            }
          })
        }
      ]
      this.dataHum = [
        {
          name: "Humidité",
          series: response.data.measures.map(measure => {
            return {
              name: new Date(measure.time),
              value: measure.humidity
            }
          })
        }
      ]
    })
  }

  @HostListener('window:resize', ['$event'])
  onResize() {
    this.view = [window.innerWidth * 0.95, window.innerHeight / 2 * 0.95]
  }
}
