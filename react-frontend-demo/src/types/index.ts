// 定义类型
export interface Item {
  id: number;
  title: string;
  description?: string;
  price: number;
  tax?: number;
  is_active: boolean;
}

export interface ItemCreate {
  title: string;
  description?: string;
  price: number;
  tax?: number;
}
