export interface Build {
  /**
   * @default {}
   */
  args?: { [key: string]: any; };

  /**
   * @default {}
   */
  build_from?: {
      /**
       * @TJS-pattern ^([a-zA-Z\-\.:\d{}]+/)*?([\-\w{}]+)/([\-\w{}]+)(:[\.\-\w{}]+)?$
       * @default homeassistant/aarch64-base:latest
       */
      aarch64?: string;

      /**
       * @TJS-pattern ^([a-zA-Z\-\.:\d{}]+/)*?([\-\w{}]+)/([\-\w{}]+)(:[\.\-\w{}]+)?$
       * @default homeassistant/amd64-base:latest
       */
      amd64?: string;

      /**
       * @TJS-pattern ^([a-zA-Z\-\.:\d{}]+/)*?([\-\w{}]+)/([\-\w{}]+)(:[\.\-\w{}]+)?$
       * @default homeassistant/armhf-base:latest
       */
      armhf?: string;

      /**
       * @TJS-pattern ^([a-zA-Z\-\.:\d{}]+/)*?([\-\w{}]+)/([\-\w{}]+)(:[\.\-\w{}]+)?$
       * @default homeassistant/armv7-base:latest
       */
      armv7?: string;

      /**
       * @TJS-pattern ^([a-zA-Z\-\.:\d{}]+/)*?([\-\w{}]+)/([\-\w{}]+)(:[\.\-\w{}]+)?$
       * @default homeassistant/i386-base:latest
       */
      i386?: string;
  };

  /**
   * @default false
   */
  squash?: boolean;
}
