Given a list of the daily opening hours for a business -- opening and closing time for each day of the week -- format the opening hours in a concise fashion for display.

Examples:

- Input:

  ```
  [
    ['9:00', '5:00'], # Monday
    ['9:00', '5:00'], # Tuesday
    ['9:00', '5:00'], # ...
    ['9:00', '5:00'],
    ['9:00', '5:00'],
    ['9:00', '5:00'],
    ['9:00', '5:00'],
  ]
  ```

  Output:

  ```
  M-Su: 9:00-5:00
  ```

- Input:

  ```
  [
    ['9:00', '5:00'], # Monday
    ['9:00', '5:00'], # Tuesday
    ['9:00', '5:00'], # ...
    ['9:00', '5:00'],
    ['9:00', '5:00'],
    ['12:00', '5:00'],
    ['12:00', '5:00'],
  ]
  ```

  Output:
  ```
  M-F: 9:00-5:00
  Sa-Su: 12:00-5:00
  ```

- Input:

  ```
  [
    ['8:00', '4:00'], # Monday
    ['9:00', '5:00'], # Tuesday
    ['8:00', '4:00'], # ...
    ['9:00', '5:00'],
    ['8:00', '4:00'],
    ['12:00', '5:00'],
    ['12:00', '5:00'],
  ]
  ```
  
  Output:
  ```
  M, W, F: 8:00-4:00
  Tu, Th: 9:00-5:00
  Sa-Su: 12:00-5:00
  ```

- Input:

  ```
  [
    ['8:00', '4:00'], # Monday
    ['8:00', '4:00'], # Tuesday
    ['8:00', '4:00'], # ...
    ['9:00', '5:00'],
    ['8:00', '4:00'],
    ['12:00', '5:00'],
    ['12:00', '5:00'],
  ]
  ```

  Output:
  ```
  M-W, F: 8:00-4:00
  Th: 9:00-5:00
  Sa-Su: 12:00-5:00
  ```
