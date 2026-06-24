import { Component, HostListener, OnInit } from '@angular/core'
import { NgxChartsModule } from "@swimlane/ngx-charts"
import { Chart } from '../../models'
import { ApiService } from '../../services/api.service'


var mockTemp = [
   { name: new Date(2026, 6, 12, 14, 4, 1), value: 21.7351913452148},
   { name: new Date(2026, 6, 12, 13, 54, 1), value: 21.7000961303711},
   { name: new Date(2026, 6, 12, 13, 44, 1), value: 21.7094421386719},
   { name: new Date(2026, 6, 12, 13, 34, 1), value: 21.7424392700195},
   { name: new Date(2026, 6, 12, 13, 24, 1), value: 21.7351913452148},
   { name: new Date(2026, 6, 12, 13, 14, 1), value: 21.7378616333008},
   { name: new Date(2026, 6, 11, 13, 4, 1), value: 21.7401504516602},
   { name: new Date(2026, 6, 11, 12, 54, 1), value: 21.7023849487305},
   { name: new Date(2026, 6, 11, 12, 44, 1), value: 21.7145919799805},
   { name: new Date(2026, 6, 11, 12, 34, 1), value: 21.7550277709961},
   { name: new Date(2026, 6, 11, 12, 24, 1), value: 21.8166351318359},
   { name: new Date(2026, 6, 10, 12, 14, 1), value: 21.8711853027344},
   { name: new Date(2026, 6, 10, 12, 4, 1), value: 21.7105865478516},
   { name: new Date(2026, 6, 10, 11, 54, 1), value: 21.4044570922852},
   { name: new Date(2026, 6, 10, 11, 44, 1), value: 20.9753036499023},
   { name: new Date(2026, 6, 10, 11, 34, 1), value: 20.5825805664063},
   { name: new Date(2026, 6, 8, 11, 24, 1), value: 20.4055786132813},
   { name: new Date(2026, 6, 8, 11, 14, 1), value: 20.4416275024414},
   { name: new Date(2026, 6, 8, 11, 4, 1), value: 20.4109191894531},
   { name: new Date(2026, 6, 8, 10, 54, 1), value: 20.4013824462891},
   { name: new Date(2026, 6, 8, 10, 44, 1), value: 20.269775390625},
   { name: new Date(2026, 6, 8, 10, 34, 1), value: 20.2674865722656},
   { name: new Date(2026, 6, 8, 10, 24, 1), value: 20.2682495117188},
   { name: new Date(2026, 6, 8, 10, 14, 1), value: 20.2241897583008},
   { name: new Date(2026, 6, 8, 10, 4, 1), value: 20.1913833618164},
   { name: new Date(2026, 6, 8, 9, 54, 1), value: 20.1269149780273},
   { name: new Date(2026, 6, 7, 9, 44, 1), value: 20.1023101806641},
   { name: new Date(2026, 6, 7, 9, 34, 1), value: 20.0502395629883},
]

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

  formatXAxis(val: any): string {
    if (val instanceof Date) {
      // Affichera par exemple "19 juin" ou "ven. 19" selon tes besoins
      return val.toLocaleDateString('fr-FR', { day: 'numeric', month: 'numeric', hour: '2-digit' });
    }
    return val;
  }
}
