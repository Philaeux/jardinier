export interface Measure {
    time: Date
    temperature: number
    humidity: number
}

export interface ChartPoint {
    name: Date
    value: number
}

export interface Chart {
    name: String
    series: ChartPoint[]
}