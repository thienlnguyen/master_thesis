<template>
  <div class="status-bar-iphone"></div>
  <DateBarHeader
    class="date-header"
    v-if="!$route.meta.hideHeaderFooter"
    :selectedDate="selectedDate"
    @update-date="updateDate"
  />
  <RemoveBarHeader class="remove-header" v-if="$route.meta.hideHeaderFooter" />
  <RouterView
    class="view"
    :selectedDate="selectedDate"
    @update-date="updateDate"
  />
  <FooterBar class="footerbar" v-if="!$route.meta.hideHeaderFooter" />
</template>

<script>
import DateBarHeader from "./components/DateBarHeader.vue";
import RemoveBarHeader from "./components/RemoveBarHeader.vue";
import FooterBar from "./components/FooterBar.vue";

import { format, addDays, parse } from "date-fns";
import { de } from "date-fns/locale";

export default {
  components: { DateBarHeader, RemoveBarHeader, FooterBar },
  data() {
    return {
      selectedDate: format(new Date(), "dd.MM.yyyy", { locale: de })
    };
  },
  methods: {
    updateDate(days) {
      const parsedDate = parse(this.selectedDate, "dd.MM.yyyy", new Date());
      if (isNaN(parsedDate)) {
        console.error("Fehler beim Parsen des Datums:", this.selectedDate);
        return;
      }
      this.selectedDate = format(addDays(parsedDate, days), "dd.MM.yyyy", { locale: de });
    }
  }
};
</script>

<style scoped>
.view {
  margin-top: 4rem;
}
</style>
