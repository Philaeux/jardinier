import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-index',
  imports: [],
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
}
